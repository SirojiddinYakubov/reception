from rest_framework import serializers

from api.v1.user.serializers import CarTypesListSerializer, UserShortDetailSerializer, OrganizationDetailSerializer
from service.models import (
    Service, StateDutyPercent, AmountBaseCalculation, ROAD_FUND, ROAD_FUND_HORSE_POWER, STATE_DUTY_TITLE,
    StateDutyScore, PaymentForTreasury, ExampleDocument
)


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'short_title',
            'long_title',
            'key',
        ]


class ServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'short_title',
            'long_title',
            'key',
            'is_active',
            'desc',
            'photo',
            'deadline',
            'instruction',
            'document',
            'created_date',
            'sort',
        ]


class StateDutyPercentDetailSerializer(serializers.ModelSerializer):
    # service = ServiceListSerializer(many=True)
    # car_type = CarTypesListSerializer(many=True)

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
        engine_power = self.context['engine_power']
        price = self.context['price']

        amount_base_calculation = AmountBaseCalculation.objects.filter(is_active=True).order_by('-id').last()
        try:
            if instance.state_duty == ROAD_FUND:
                payment = round(round(instance.percent, 2) / 100 * round(int(price), 2), 2)
            elif instance.state_duty == ROAD_FUND_HORSE_POWER:
                payment = round(amount_base_calculation.amount / 100 * round(instance.percent, 2) * int(engine_power),
                                2)
            else:
                payment = amount_base_calculation.amount / 100 * round(instance.percent, 2)
            context['amount'] = round(payment, 2)

        except Exception as e:
            print(e)
            context['amount'] = instance.percent
        context['state_duty'] = dict(STATE_DUTY_TITLE).get(context['state_duty'])
        context['bhm'] = amount_base_calculation.amount
        if self.context.get('applicant'):
            context['applicant'] = UserShortDetailSerializer(self.context['applicant']).data
        if self.context.get('organization'):
            context['organization'] = OrganizationDetailSerializer(self.context.get('organization')).data
        return context


class StateDutyPercentDetailShortSerializer(serializers.ModelSerializer):
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


class StateDutyScoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = StateDutyScore
        fields = [
            'id',
            'state_duty',
            'region',
            'district',
            'score',
            'created_date'
        ]


class StateDutiesListSerializer(serializers.Serializer):
    title = serializers.ListSerializer(child=StateDutyScoreDetailSerializer())


class PaymentForTreasuryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentForTreasury
        fields = [
            'id',
            'application',
            'amount',
            'state_duty_score',
            'state_duty_percent',
            'amount_base_calculation',
            'memorial',
            'payment_system',
            'transaction_id',
            'status'
        ]
    def to_representation(self, instance):
        context = super(PaymentForTreasuryListSerializer, self).to_representation(instance)
        context['state_duty_title'] = dict(STATE_DUTY_TITLE).get(instance.state_duty_percent.state_duty)
        if instance.state_duty_score:
            score = StateDutyScore.objects.get(id=instance.state_duty_score.id).score
            context['score'] = score
        context['title'] = instance.state_duty_percent.title
        return context

class ExampleDocumentDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExampleDocument
        fields = [
            'id',
            'title',
            'key'
        ]


class StateDutiesReportSerializer(serializers.Serializer):
    title = serializers.CharField()
    total_amount = serializers.IntegerField()

