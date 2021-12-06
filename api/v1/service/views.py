from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1 import permissions
from api.v1.service import serializers
from application.models import (Application)
from service.models import (
    Service, StateDutyPercent
)


class ServiceList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.ServiceListSerializer
    queryset = Service.objects.filter(is_active=True)


class StateDutyPercentDetail(generics.RetrieveAPIView):
    permission_classes = [permissions.UserPermission]
    serializer_class = serializers.StateDutyPercentDetailSerializer
    queryset = StateDutyPercent.objects.all()

    def get_serializer_context(self):
        application = Application.objects.get(id=self.request.GET.get('application'))
        context = super(StateDutyPercentDetail, self).get_serializer_context()
        context.update({"request": self.request})
        context.update({"engine_power": application.car.engine_power})
        context.update({"price": application.car.price})
        context.update({'applicant': application.applicant})
        return context