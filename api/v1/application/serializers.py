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
    Application
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
        if data.get('person_type', None):
            if not data.get('organization'):
                raise serializers.ValidationError('Tashkilot topilmadi!')
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
