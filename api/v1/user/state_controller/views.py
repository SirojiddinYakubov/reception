from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from application.models import (Application, ACCEPTED_FOR_CONSIDERATION, WAITING_FOR_PAYMENT,
                                WAITING_FOR_ORIGINAL_DOCUMENTS, REJECTED, ACCEPTED)
from . import serializers
from api.v1 import permissions
from application.models import (SHIPPED)
from .import filters


class ApplicationsList(generics.ListAPIView):
    queryset = Application.objects.filter(is_active=True)
    serializer_class = serializers.ApplicationsListSerializer
    filter_class = filters.ApplicationRightFilter
    pagination_class = LimitOffsetPagination
    max_page_size = 10

    permission_classes = [
        permissions.StateControllerPermission
    ]

    def get_queryset(self):
        qs = super(ApplicationsList, self).get_queryset()
        return qs
