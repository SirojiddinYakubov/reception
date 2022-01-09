from rest_framework import serializers

from api.v1.service.serializers import (
    ServiceDetailSerializer
)
from api.v1.user.serializers import (
    UserShortDetailSerializer,
    OrganizationDetailSerializer,
    CarDetailSerializer
)
from application.models import (
    Application, ApplicationDocument
)


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