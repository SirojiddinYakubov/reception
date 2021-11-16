from rest_framework import serializers

from .models import (
    DocumentForPolice,
    Application
)


class DocumentForPoliceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentForPolice
        fields = ['id', 'title', 'service', 'is_active']


class SaveDraftApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        fields = ['organization', '']
