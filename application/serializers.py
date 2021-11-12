from rest_framework import serializers

from .models import DocumentForPolice


class DocumentForPoliceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentForPolice
        fields = ['id', 'title', 'service', 'is_active']
