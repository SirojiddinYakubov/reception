from rest_framework import serializers

from api.v1.service.serializers import (
    ServiceDetailSerializer, ExampleDocumentDetailSerializer, StateDutyScoreDetailSerializer,
    PaymentForTreasuryListSerializer
)
from api.v1.user.serializers import (
    UserShortDetailSerializer,
    OrganizationDetailSerializer,
    CarDetailSerializer, SectionDetailSerializer, UserDetailSerializer
)
from application.models import (
    Application, ApplicationDocument, DocumentForPolice
)
from application.serializers import DocumentForPoliceSerializer
from application.templatetags.applications_tags import get_payment_score
from reception.api import SendSmsWithPlayMobile, SUCCESS, SendSmsWithApi
from reception.telegram_bot import send_message_to_developer
from service.models import STATE_DUTY_TITLE, ROAD_FUND_HORSE_POWER, ROAD_FUND, AmountBaseCalculation, StateDutyPercent, \
    StateDutyScore, PaymentForTreasury
from user.models import User, CHECKER


class CreateApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'id',
            'person_type',
            'organization',
            'service',
            'applicant',
            'car',
        ]
        extra_kwargs = {
            'person_type': {'required': True},
            'service': {'required': True},
            'applicant': {'required': True},
            'car': {'required': True},
        }

    def validate(self, data):
        errors = dict()

        if data.get('person_type', None):
            if not data.get('organization'):
                errors.update(organization=["Ushbu maydon to'ldirilishi shart."])

        if errors.__len__() > 0:
            raise serializers.ValidationError(errors)

        return data

    def create(self, validated_data):
        validated_data['created_user'] = self.context.user
        return super().create(validated_data)

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['service'] = ServiceDetailSerializer(instance.service).data
        context['applicant'] = UserShortDetailSerializer(instance.applicant).data
        context['car'] = CarDetailSerializer(instance.car).data
        if context.get('organization'):
            context['organization'] = OrganizationDetailSerializer(instance.organization).data
        return context


class CreateApplicationDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApplicationDocument
        fields = [
            'id',
            'application',
            'example_document',
            'seriya',
            'contract_date'
        ]

    def create(self, validated_data):
        return super().create(validated_data)

class ApplicationDocumentDetailSerializer(serializers.ModelSerializer):
    example_document = ExampleDocumentDetailSerializer()
    class Meta:
        model = ApplicationDocument
        fields = [
            'id',
            'application',
            'example_document',
            'seriya',
            'contract_date'
        ]


class ApplicationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'id',
            'service',
            'created_user',
            'person_type',
            'organization',
            'process',
            'is_payment',
            'file_name',
            'password',
            'given_date',
            'given_time',
            'is_active',
            'is_block',
            'cron',
            'section',
            'car',
            'created_date',
            'updated_date',
            'canceled_date',
            'confirmed_date',
            'inspector',
            'applicant'
        ]


class ApplicationDetailFullSerializer(serializers.ModelSerializer):
    service = ServiceDetailSerializer()
    created_user = UserShortDetailSerializer()
    applicant = UserDetailSerializer()
    inspector = UserShortDetailSerializer()
    car = CarDetailSerializer()

    class Meta:
        model = Application
        fields = [
            'id',
            'service',
            'created_user',
            'person_type',
            'organization',
            'process',
            'is_payment',
            'file_name',
            'password',
            'given_date',
            'given_time',
            'is_active',
            'is_block',
            'cron',
            'section',
            'car',
            'created_date',
            'updated_date',
            'canceled_date',
            'confirmed_date',
            'inspector',
            'applicant'
        ]

    def to_representation(self, instance):
        context = super().to_representation(instance)
        if instance.organization:
            context['organization'] = OrganizationDetailSerializer(instance.organization).data

        if instance.section:
            context['section'] = SectionDetailSerializer(instance.section).data

        if instance.applicationdocument_set.exists():
            context['document'] = ApplicationDocumentDetailSerializer(instance.applicationdocument_set.last()).data

        document_polices = DocumentForPolice.objects.filter(is_active=True, service=instance.service)
        context['requireDocuments'] = DocumentForPoliceSerializer(document_polices, many=True).data
        return context

class ApplicationSectionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = [
            'process',
            'section',
        ]

    def update(self, instance, validated_data):
        application = super(ApplicationSectionUpdateSerializer, self).update(instance, validated_data)

        text = f"E-RIB.UZ Onlayn ariza platformasiga {application.id}-raqamli ariza kelib tushdi. \nIltimos arizani ko'rib chiqish uchun qabul qiling. Fuqaro sizning javobingizni kutmoqda! \nAvtomobil: {application.car}"
        inspectors = User.objects.filter(section=application.section, role__in=[CHECKER])

        if inspectors:
            for inspector in inspectors:
                r = SendSmsWithPlayMobile(phone=inspector.phone, message=text).get()
                if not r == SUCCESS:
                    r = SendSmsWithApi(message=text, phone=inspector.phone).get()
                    if not r == SUCCESS:
                        send_message_to_developer('Sms service not working!')
        return application


class ApplicationPaymentStateDutyPercentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateDutyPercent
        fields = [
            'id',
            'title',
            'service',
            'state_duty',
            'person_type',
            'car_type',
            'car_is_new',
            'is_old_number',
            'is_save_old_number',
            'lost_number',
            'lost_technical_passport',
            'is_auction',
            'is_tranzit',
            'start',
            'stop',
            'percent',
        ]

    def to_representation(self, instance):
        context = super().to_representation(instance)
        application = self.context.get('application')
        amount_base_calculation = AmountBaseCalculation.objects.filter(is_active=True).order_by('-id').last()
        try:
            payment = amount_base_calculation.amount / 100 * round(instance.percent, 2)
            context['amount'] = round(payment, 2)
        except Exception as e:
            print(e)

        if context.get('state_duty'):
            context['state_duty_title'] = dict(STATE_DUTY_TITLE).get(context['state_duty'])
        context['bhm'] = amount_base_calculation.amount

        if application.section:
            score = get_payment_score(application.id, context['id'])
            if isinstance(score, StateDutyScore):
                context['score'] = StateDutyScoreDetailSerializer(score).data
            else:
                context['score'] = score
        context['check_state_payment_paid'] = application.paymentfortreasury_set.filter(state_duty_percent_id=context['id']).exists()
        check_memorial = PaymentForTreasury.objects.filter(state_duty_percent_id=context['id'], application=application,
                                             memorial__isnull=False).last()
        if check_memorial:
            context['check_memorial'] = PaymentForTreasuryListSerializer(check_memorial).data
        return context