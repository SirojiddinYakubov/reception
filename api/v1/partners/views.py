from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.partners import serializers
from partners.models import (DiagnosticDepartment)

class DistrictDiagnosticsList(APIView):
    queryset = DiagnosticDepartment.objects.filter(is_active=True)
    serializer_class = serializers.DistrictDiagnosticsListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return self.queryset.filter(region_id=self.kwargs.get('pk'))
