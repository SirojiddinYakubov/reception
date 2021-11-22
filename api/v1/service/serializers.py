from rest_framework import serializers
from service.models import (
    Service
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
