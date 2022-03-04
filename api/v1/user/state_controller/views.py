import datetime

from django.db.models import Sum, F
from rest_framework import generics, status
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from application.models import (Application, ACCEPTED_FOR_CONSIDERATION, WAITING_FOR_PAYMENT,
                                WAITING_FOR_ORIGINAL_DOCUMENTS, REJECTED, ACCEPTED)
from reception.settings import LOCAL_TIMEZONE
from service.models import PaymentForTreasury, STATE_DUTY_TITLE
from . import serializers
from api.v1 import permissions
from application.models import (SHIPPED)
from .import filters
from ...filters import PaymentsListFilter
from ...serializers import PaymentForTreasuryListSerializer


class ApplicationsList(generics.ListAPIView):
    queryset = Application.objects.filter(is_active=True)
    serializer_class = serializers.ApplicationsListSerializer
    filter_class = filters.ApplicationRightFilter
    pagination_class = LimitOffsetPagination
    max_page_size = 10

    permission_classes = [
        permissions.StateControllerPermission
    ]

    def get_queryset(self):
        qs = super(ApplicationsList, self).get_queryset()
        return qs


class PaymentsList(generics.ListAPIView):
    queryset = PaymentForTreasury.objects.filter(is_active=True)
    serializer_class = PaymentForTreasuryListSerializer
    filter_class = PaymentsListFilter
    pagination_class = LimitOffsetPagination
    max_page_size = 10

    permission_classes = [
        permissions.RegionalControllerPermission |
        permissions.StateControllerPermission
    ]

    def get_queryset(self):
        qs = super().get_queryset().filter(status__in=[PaymentForTreasury.SUCCESS,
                                                       PaymentForTreasury.CANCELED,
                                                       PaymentForTreasury.FAILED])
        return qs


class StateDutiesReport(APIView):
    permission_classes = [
        permissions.RegionalControllerPermission |
        permissions.StateControllerPermission
    ]
    serializer_class = PaymentForTreasuryListSerializer

    def get_queryset(self, request, *args, **kwargs):
        qs = PaymentForTreasury.objects.filter(is_active=True, status=PaymentForTreasury.SUCCESS,
                                               memorial__isnull=False)
        region_id = request.GET.get('region')
        section_id = request.GET.get('section')
        start_date = request.GET.get('start_date')
        end_date = request.GET.get('end_date')

        # today_min = timezone.now().replace(tzinfo=LOCAL_TIMEZONE, hour=0, minute=0, second=0)
        # today_max = timezone.now().replace(tzinfo=LOCAL_TIMEZONE, hour=23, minute=59, second=59)

        if region_id:
            qs = qs.filter(application__section__region_id=region_id)

        if section_id:
            qs = qs.filter(application__section_id=section_id)

        start_min = datetime.datetime.strptime(start_date, "%Y-%m-%d").replace(tzinfo=LOCAL_TIMEZONE) if start_date else datetime.datetime.now().replace(tzinfo=LOCAL_TIMEZONE, day=1, month=1, year=2020)
        end_max = datetime.datetime.strptime(end_date, "%Y-%m-%d").replace(tzinfo=LOCAL_TIMEZONE) if end_date else datetime.datetime.now().replace(tzinfo=LOCAL_TIMEZONE)
        qs = qs.filter(created_at__range=[start_min, end_max])
        return qs

    def get(self, request, *args, **kwargs):
        # for title, items in itertools.groupby(qs, lambda x: dict(STATE_DUTY_TITLE).get(x.state_duty_percent.state_duty)):
        # for q in qs:
        #     state_duties.setdefault(q.state_duty_percent.get_state_duty_display(), []).append(q)
        results = self.get_queryset(request, *args, **kwargs).values(title=F('state_duty_percent__state_duty')) \
            .order_by('title') \
            .annotate(total_amount=Sum('amount'))

        for result in results:
            result['title'] = dict(STATE_DUTY_TITLE).get(result['title'])
        return Response(list(results), status=status.HTTP_200_OK)