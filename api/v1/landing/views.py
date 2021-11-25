from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.landing import serializers
from api.v1.service.serializers import StateDutyPercentDetailSerializer
from application.utils import filter_state_duty_percents


class Calculate(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = serializers.CalculateSerializer(data=request.data)
        if serializer.is_valid():
            engine_power = serializer.data.get('engine_power')
            price = serializer.data.get('price')
            qs = filter_state_duty_percents(serializer.data)
            state_duty_percent_serializer = StateDutyPercentDetailSerializer(qs, many=True,
                                                                             context={'engine_power': engine_power,
                                                                                      'price': price})
            return Response(state_duty_percent_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
