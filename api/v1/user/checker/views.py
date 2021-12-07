from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from application.models import (Application, ACCEPTED_FOR_CONSIDERATION, WAITING_FOR_PAYMENT,
                                WAITING_FOR_ORIGINAL_DOCUMENTS, REJECTED, ACCEPTED)
from user.models import (Section)
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
        permissions.CheckerPermission
    ]

    def get_queryset(self):
        section = Section.objects.get(id=self.request.user.section.id)
        qs = super(ApplicationsList, self).get_queryset().filter(section=section, is_block=False).filter(
            process__in=[SHIPPED, ACCEPTED_FOR_CONSIDERATION, WAITING_FOR_PAYMENT, WAITING_FOR_ORIGINAL_DOCUMENTS,
                         ACCEPTED, REJECTED])
        return qs
