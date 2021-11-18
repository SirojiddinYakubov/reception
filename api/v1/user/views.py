from rest_framework import generics
from api.v1 import permissions
from api.v1.user import serializers
from user.models import (
    User,
    Organization, CarModel, Color
)


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]


class UserOrganizationsList(generics.ListAPIView):
    queryset = Organization.objects.filter(is_active=True)
    serializer_class = serializers.UserOrganizationsListSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]

    def get_queryset(self):
        qs = super().get_queryset().filter(applicant=self.request.user)
        return qs

class CreateOrganization(generics.CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = serializers.CreateOrganizationSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]

class CreateCarModel(generics.CreateAPIView):
    queryset = CarModel.objects.filter(is_active=True)
    serializer_class = serializers.CreateCarModelSerializer
    permission_classes = [
            permissions.UserPermission |
            permissions.AppCreatorPermission
    ]

class CreateColor(generics.CreateAPIView):
    queryset = Color.objects.filter(is_active=True)
    serializer_class = serializers.CreateColorSerializer
    permission_classes = [
            permissions.UserPermission |
            permissions.AppCreatorPermission
    ]