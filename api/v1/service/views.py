from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1 import permissions
from api.v1.service import serializers
from service.models import (
    Service
)


class ServiceList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.ServiceListSerializer
    queryset = Service.objects.filter(is_active=True)


class Calculate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        print(request.data)
        return Response({'status': 'OK'}, status=status.HTTP_200_OK)
