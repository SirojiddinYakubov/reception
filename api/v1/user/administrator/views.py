from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1 import permissions
from reception.api import PaymentByRequisites, SUCCESS
from user.models import (User, USER, Balance)
from . import filters
from . import serializers
from api.v1.user.serializers import UserListSerializer


class ApplicantsList(generics.ListAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserListSerializer
    filter_class = filters.ApplicantsRightFilter
    pagination_class = LimitOffsetPagination
    max_page_size = 10

    permission_classes = [
        permissions.AdministratorPermission
    ]

    def get_queryset(self):
        qs = super(ApplicantsList, self).get_queryset().filter(is_superuser=False, is_staff=False,
                                                               role__in=[USER]).order_by('-id')
        return qs


class AccountBalance(APIView):
    def get(self, request, *args, **kwargs):
        account_balance = PaymentByRequisites().account_balance()
        if account_balance['status'] == SUCCESS:
            balance = int(account_balance['result']) / 100
            Balance.objects.create(amount=balance)
            return Response(balance, status=status.HTTP_200_OK)
        else:
            return Response(account_balance['result'], status=status.HTTP_400_BAD_REQUEST)
