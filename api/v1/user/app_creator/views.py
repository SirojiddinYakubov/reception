from rest_framework import generics
from . import serializers
from api.v1 import permissions
from user.models import (
    Organization
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
