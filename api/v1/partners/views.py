from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from api.v1.partners import serializers, filters
from partners.models import (DiagnosticDepartment)

class DiagnosticsList(generics.ListAPIView):
    queryset = DiagnosticDepartment.objects.filter(is_active=True).order_by('?')
    serializer_class = serializers.DiagnosticsListSerializer
    filter_class = filters.DiagnosticsListFilter
    pagination_class = LimitOffsetPagination
    max_page_size = 10
    permission_classes = [AllowAny]


