import time
from datetime import datetime
from rest_framework import generics
import pytz
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from . import serializers, filters
from driver_license.models import CallToExam
from reception.api import SendSmsWithPlayMobile, SUCCESS, SendSmsWithApi
from reception.settings import TIME_ZONE
from reception.telegram_bot import send_message_to_developer


class CallToExamSendSms(APIView):
    permission_classes = [
        AllowAny
    ]

    def post(self, request, *args, **kwargs):
        print(request.POST)
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        coming_date = request.POST.get('coming_date')
        coming_time = request.POST.get('coming_time')
        secret_key = request.POST.get('secret_key')

        if secret_key != 'avtoustoz':
            return Response("Maxfiy kod noto'g'ri!", status=status.HTTP_400_BAD_REQUEST)

        date = datetime.strptime(f'{coming_date} {coming_time}', '%Y-%m-%d %H:%M').replace(
            tzinfo=pytz.timezone(TIME_ZONE))
        call_to_exam = CallToExam.objects.create(coming_date=date, pupil=name, phone=phone)

        text = f"Hurmatli {name}, Sizni {coming_date} sanasi, {coming_time} da haydovchilik guvohnomasi imtihoniga kelishingizni so'raymiz! Manzil: Buxoro viloyati, Kogon tumani, Bog'i bolo qishlog'i (https://goo.gl/maps/bAPJzxfeUzLAPCwPA)"
        r = SendSmsWithPlayMobile(phone=phone, message=text).get()

        if not r == SUCCESS:
            # send sms with eskiz
            r = SendSmsWithApi(message=text, phone=phone).get()

        if r != SUCCESS:
            send_message_to_developer(f'Sms service not working!')
            return Response("Sms jo'natishda xatolik!", status=status.HTTP_400_BAD_REQUEST)
        call_to_exam.is_send = True
        call_to_exam.save()
        return Response(status=status.HTTP_200_OK)


class CallToExamSendSmsList(generics.ListAPIView):
    queryset = CallToExam.objects.filter(is_active=True).order_by('-id')
    serializer_class = serializers.CallToExamSendSmsListSerializer
    filter_class = filters.CallToExamSendSmsListFilter
    pagination_class = LimitOffsetPagination
    max_page_size = 10
    permission_classes = [AllowAny]
