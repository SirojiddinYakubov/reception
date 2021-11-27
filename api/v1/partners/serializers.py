from rest_framework import serializers
from partners.models import (DiagnosticDepartment)


class DistrictDiagnosticsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticDepartment
        fields = [
            'id',
            'region',
            'district',
            'address',
            'longitude',
            'latitude',
            'title',
            'phone'
        ]
