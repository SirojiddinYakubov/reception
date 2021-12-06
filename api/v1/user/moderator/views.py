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

        pay_treasury_payload = json.dumps({
            "method": "receipt.pay_requisite",
            "params": {
                "account": pay.state_duty_score.score,
                "mfo": "00014",
                "name": f"{pay.application.applicant.last_name} {pay.application.applicant.first_name} {pay.application.applicant.middle_name}",
                "details": f" {pay.state_duty_percent.title.upper()} (E-RIB.UZ 308944250)",
                "amount": pay.amount * 100,
                "senderName": f"{pay.application.applicant.last_name.upper()} {pay.application.applicant.first_name.upper()} {pay.application.applicant.middle_name.upper()}",
                "transactionId": pay.transaction_id
            }
        })
        pay_treasury = requests.request("POST", url="https://topup.apelsin.uz/api/merchant/", data=pay_treasury_payload,
                                        headers={'Content-type': 'application/json'},
                                        auth=(os.getenv('APELSIN_USERNAME'), os.getenv('APELSIN_PASSWORD')))

        """
        success:
        {'receipt': 
            {
            '_id': '8be8b1cff59d4281888ba2825a0d3967', 
            'state': 30, 
            'create_date': 1638719484991, 
            'pay_date': 1638719486245, 
            'error': None, 'type': 7, 
            'card': {'sender_id': '29896000705447577002'}, 
            'merchant': None, 
            'description': None, 
            'account': None, 
            'detail': 
                {   
                    "account": "20208000305447577001",
                    "mfo":"00966",
                    "name": "hjghj1 hjghjg1 ghjghj1",
                    "details":"Qayta ro\'yhatlash uchun to\'lov (E-RIB.UZ 308944250)",
                    "senderName":"OOO OPENSOFT",
                    "memorial":"https://ek.apelsin.uz/memorial?id=RX%2Bq4L%2FXxo2kOc6%2FUgUQ5jXNmoNfGxXLpyLe%2BSE3Zc4PI0FpRjY33bdMH8BX%2FevW",
                    "externalTransactionId":"1638719626"
                }', 
            'amount': 101000, 
            'currency': 860, 
            'commission': 1000
            }
        }
        """

        try:
            if 'error' in pay_treasury.json():
                if pay_treasury.json()['error'] == 'External id exists':
                    print('105')
                    return Response("Xatolik! Bunday ID raqamli to'lov avval amalga oshirilgan!",
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                print('109')
                if pay_treasury.json()['receipt']['state'] == 30:
                    print('111')
                    memorial = json.loads(pay_treasury.json()['receipt']['detail'])
                    memorial = memorial['memorial']
                    memorial = memorial.replace("memorial", 'pdf')
                    pay.status = PaymentForTreasury.SUCCESS
                    pay.memorial = memorial
                    pay.save()
                    return Response({'OK': True}, status=status.HTTP_200_OK)
                else:
                    print('117')
                    return Response({'Failed': True}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print('120')
            send_message_to_developer(f"error: {e}")
            return Response({'Failed': True}, status=status.HTTP_400_BAD_REQUEST)
