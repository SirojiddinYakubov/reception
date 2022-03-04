import itertools
import json

from django.db.models import Sum, F
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1 import permissions
from api.v1.service import serializers
from application.models import (Application)
from service.models import (
    Service, StateDutyPercent, PaymentForTreasury, STATE_DUTY_TITLE
)


class ServiceList(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.ServiceListSerializer
    queryset = Service.objects.filter(is_active=True)


class StateDutyPercentDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = serializers.StateDutyPercentDetailSerializer
    queryset = StateDutyPercent.objects.all()

    def get_serializer_context(self):
        application = Application.objects.get(id=self.request.GET.get('application'))
        context = super(StateDutyPercentDetail, self).get_serializer_context()
        context.update({"request": self.request})
        context.update({"engine_power": application.car.engine_power})
        context.update({"price": application.car.price})
        if application.applicant:
            context.update({'applicant': application.applicant})
        else:
            context.update({'applicant': application.created_user})
        return context


class RegionStateDutiesList(APIView):
    permission_classes = [
        permissions.RegionalControllerPermission
    ]
    serializer_class = serializers.StateDutiesListSerializer

    def get_queryset(self, request, *args, **kwargs):
        qs = PaymentForTreasury.objects.filter(is_active=True, status=PaymentForTreasury.SUCCESS,
                                               memorial__isnull=False)
        section_id = request.GET.get('section')
        if section_id:
            return qs.filter(application__section_id=section_id)
        else:
            return qs.filter(application__section__region=self.kwargs.get('id'))
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


class PaymentForTreasuryList(generics.ListAPIView):
    permission_classes = [
        permissions.RegionalControllerPermission
    ]
    serializer_class = serializers.PaymentForTreasuryListSerializer
    queryset = PaymentForTreasury.objects.all()

    def get_queryset(self):
        qs = super().get_queryset()
        return qs
