from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination

from . import serializers, filters
from api.v1 import permissions
from user.models import (
    Organization, User, USER
)



class UserOrganizationsList(generics.ListAPIView):
    queryset = Organization.objects.filter(is_active=True)
    serializer_class = serializers.UserOrganizationsListSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]

    def get_queryset(self):
        applicant_id = self.kwargs.get('pk')
        qs = super().get_queryset().filter(created_user=self.request.user, applicant_id=applicant_id)
        return qs


class SelfCreatedUsersList(generics.ListAPIView):
    queryset = User.objects.filter(passport_seriya__isnull=False, passport_number__isnull=False,
                                   issue_by_whom__isnull=False)
    serializer_class = serializers.SelfCreatedUsersListSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]

    def get_queryset(self):
        qs = super().get_queryset().filter(created_by=self.request.user)
        return qs


class ApplicantsList(generics.ListAPIView):
    queryset = User.objects.filter(passport_seriya__isnull=False, passport_number__isnull=False,
                                   issue_by_whom__isnull=False, role=USER).order_by('last_name', 'first_name', 'middle_name')
    filter_class = filters.ApplicantsListFilter
    pagination_class = LimitOffsetPagination
    max_page_size = 10
    serializer_class = serializers.ApplicantListSerializer
    permission_classes = [
        permissions.AppCreatorPermission
    ]


class CreateApplicant(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.CreateApplicantSerializer
    permission_classes = [
        permissions.AppCreatorPermission
    ]