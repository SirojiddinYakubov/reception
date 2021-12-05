import json
import os

import requests
from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from application.models import (Application, ACCEPTED_FOR_CONSIDERATION, WAITING_FOR_PAYMENT,
                                WAITING_FOR_ORIGINAL_DOCUMENTS, REJECTED, ACCEPTED)
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
        pay_past = PaymentForTreasury.objects.filter(is_send=True).order_by('-transaction_id').first()
        # print(pay_past.transaction_id)

        tranzaction_id = int(pay_past.transaction_id) + 1
        pay_treasury_payload = json.dumps({
            "method": "receipt.pay_requisite",
            "params": {
                "account": "20208000305447577001",
                "mfo": "00966",
                "name": f"{pay.application.applicant.last_name} {pay.application.applicant.first_name} {pay.application.applicant.middle_name}",
                "details": pay.state_duty_percent.title,
                "amount": pay.amount,
                "senderName": "OOO OPENSOFT",
                "transactionId": tranzaction_id
            }
        })
        pay_treasury = requests.request("POST", url="https://topup.apelsin.uz/api/merchant/", data=pay_treasury_payload, headers={'Content-type': 'application/json'},
                                            auth=(os.getenv('APELSIN_USERNAME'), os.getenv('APELSIN_PASSWORD')))

        print(os.getenv('APELSIN_PASSWORD'))

        try:

            if pay_treasury.json()['error'] == 'External id exists':
                return "Xatolik! Bunday ID raqamli to'lov avval amalga oshirilgan!"
            else:
                pass
            return Response({'OK': True}, status=status.HTTP_200_OK)

        except Exception as e:
            print('except')
            send_message_to_developer(f"error: {e}")
            return Response({'Failed': True}, status=status.HTTP_200_OK)

