from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from api.v1 import permissions
from user.models import (User, USER)
from . import filters
from . import serializers
from api.v1.user.serializers import UserListSerializer


class ApplicantsList(generics.ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserListSerializer
    filter_class = filters.ApplicantsRightFilter
    pagination_class = LimitOffsetPagination
    max_page_size = 10

    permission_classes = [
        permissions.AdministratorPermission
    ]

    def get_queryset(self):
        qs = super(ApplicantsList, self).get_queryset().filter(is_superuser=False, is_staff=False,
                                                               role__in=[USER]).order_by('-id')
        return qs
