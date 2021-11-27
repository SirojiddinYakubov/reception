from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1 import permissions
from api.v1.user import serializers
from reception.telegram_bot import send_message_to_developer
from user.models import (
    User,
    Organization, CarModel, Color, CarType, FuelType, BodyType, Sms, Region, District, Quarter, Section
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


class CarModelsList(generics.ListAPIView):
    queryset = CarModel.objects.filter(is_active=True)
    serializer_class = serializers.CarModelsListSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]


class CarColorsList(generics.ListAPIView):
    queryset = Color.objects.filter(is_active=True)
    serializer_class = serializers.CarColorsListSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]


class CarTypesList(generics.ListAPIView):
    queryset = CarType.objects.filter(is_active=True)
    serializer_class = serializers.CarTypesListSerializer
    permission_classes = [AllowAny]


class RegionsList(generics.ListAPIView):
    queryset = Region.objects.filter(is_active=True)
    serializer_class = serializers.RegionDetailSerializer
    permission_classes = [AllowAny]


class RegionDistrictsList(generics.ListAPIView):
    queryset = District.objects.filter(is_active=True)
    serializer_class = serializers.DistrictDetailSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return self.queryset.filter(region_id=self.kwargs.get('pk'))


class RegionSectionsList(generics.ListAPIView):
    queryset = Section.objects.filter(is_active=True)
    serializer_class = serializers.RegionSectionsListSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]

    def get_queryset(self):
        return self.queryset.filter(region_id=self.kwargs.get('pk'))


class DistrictQuartersList(generics.ListAPIView):
    queryset = Quarter.objects.filter(is_active=True)
    serializer_class = serializers.QuarterDetailSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]

    def get_queryset(self):
        return self.queryset.filter(district_id=self.kwargs.get('pk'))


class CarFuelTypesList(generics.ListAPIView):
    queryset = FuelType.objects.filter(is_active=True)
    serializer_class = serializers.CarFuelTypesListSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]


class CarBodyTypesList(generics.ListAPIView):
    queryset = BodyType.objects.filter(is_active=True)
    serializer_class = serializers.CarBodyTypesListSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]


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


class PlayMobileSmsStatus(APIView):
    def post(self, request, *args, **kwargs):
        """пример запроса статуса:
        { “messages”: {
            “message-id”: “exb48879”,
            “channel”: “SMS”,
            “status”: “Delivered”,
            “status-date”: “2019-11-23 12:23:10”,
            “description”: “”
            }
        }
        """
        # sms = Sms.objects.filter(sms_id=)
        send_message_to_developer(str(request.POST))
        return Response({'status': 'OK'}, status=status.HTTP_200_OK)
