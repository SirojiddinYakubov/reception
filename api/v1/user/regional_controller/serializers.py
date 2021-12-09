from rest_framework import serializers

from api.v1.service.serializers import (ServiceDetailSerializer)
from api.v1.user.serializers import SectionDetailSerializer, CarDetailSerializer, UserShortDetailSerializer
from application.models import (Application)


class ApplicationsListSerializer(serializers.ModelSerializer):
    service = ServiceDetailSerializer()
    section = SectionDetailSerializer()
    car = CarDetailSerializer()
    created_user = UserShortDetailSerializer()
    class Meta:
        model = Application
        fields = [
            'id',
            'service',
            'section',
            'car',
            'created_user',
            'created_date',
            'process',

        ]

