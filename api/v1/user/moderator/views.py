import json
import os
import re

import requests
from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from application.models import (Application, ACCEPTED_FOR_CONSIDERATION, WAITING_FOR_PAYMENT,
                                WAITING_FOR_ORIGINAL_DOCUMENTS, REJECTED, ACCEPTED)
from reception.api import SendSmsWithPlayMobile, SendSmsWithApi, SUCCESS, PaymentByRequisites
from reception.telegram_bot import send_message_to_developer
from service.models import PaymentForTreasury
from . import serializers
from api.v1 import permissions
from application.models import (SHIPPED)
from . import filters


class ApplicationsList(generics.ListAPIView):
    queryset = Application.objects.filter(is_active=True)
    serializer_class = serializers.ApplicationsListSerializer
    filter_class = filters.ApplicationRightFilter
    pagination_class = LimitOffsetPagination
    max_page_size = 10

    permission_classes = [
        permissions.ModeratorPermission
    ]

    def get_queryset(self):
        qs = super(ApplicationsList, self).get_queryset()
        return qs


class PaymentsList(generics.ListAPIView):
    queryset = PaymentForTreasury.objects.filter(is_active=True)
    serializer_class = serializers.PaymentForTreasuryListSerializer
    pagination_class = LimitOffsetPagination
    max_page_size = 10

    permission_classes = [
        permissions.ModeratorPermission
    ]


class ConfirmTheasuryPayment(APIView):
    permission_classes = [
        permissions.ModeratorPermission
    ]

    def post(self, request, *args, **kwargs):
        pay = PaymentForTreasury.objects.get(id=request.POST.get('id'))

        if pay.application.applicant:
            applicant = pay.application.applicant
        else:
            applicant = pay.application.created_user

        pay_treasury_payload = json.dumps({
            "method": "receipt.pay_requisite",
            "params": {
                "account": pay.state_duty_score.score,
                "mfo": "00014",
                "name": f"{applicant.last_name} {applicant.first_name} {applicant.middle_name}",
                "details": f" {pay.application.id}-ARIZAGA ASOSAN {pay.state_duty_percent.title.upper()} (E-RIB.UZ 308944250)",
                "amount": pay.amount * 100,
                "senderName": f"{applicant.last_name.upper()} {applicant.first_name.upper()} {applicant.middle_name.upper()}",
                "transactionId": pay.transaction_id
            }
        })

        transaction = PaymentByRequisites().pay_treasury(pay, pay_treasury_payload)
        print(transaction)
        if transaction['status'] == SUCCESS:
            pay.status = PaymentForTreasury.SUCCESS
            pay.memorial = transaction['result']['memorial']
            pay.transaction_id = transaction['result']['_id']
            pay.save()
            text = f"{pay.application.id}-raqamli arizangizga muvofiq, {pay.amount} so'm muvaffaqiyatli o'tkazildi. Kvitansiyani http://e-rib.uz/en/application/application-detail/{pay.application.id} manzilidan yuklab olishingiz mumkin"

            if pay.application.applicant:
                phone = pay.application.applicant.phone
            else:
                phone = pay.application.created_user.phone

            r = SendSmsWithPlayMobile(phone=phone, message=text).get()

            if not r == SUCCESS:
                # send sms with eskiz
                r = SendSmsWithApi(message=text, phone=phone).get()

            if r != SUCCESS:
                send_message_to_developer(f'Sms service not working!')

            return Response(status=status.HTTP_200_OK)
        else:
            return Response("Xatolik! Sahifani yangilab qayta urinib ko'ring!", status=status.HTTP_400_BAD_REQUEST)
