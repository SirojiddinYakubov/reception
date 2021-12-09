from rest_framework import serializers

from api.v1.service.serializers import StateDutyScoreDetailSerializer, StateDutyPercentDetailShortSerializer
from api.v1.user.checker.serializers import ApplicationsListSerializer
from api.v1.user.serializers import UserShortDetailSerializer, DistrictDetailSerializer
from service.models import PaymentForTreasury


class PaymentForTreasuryListSerializer(serializers.ModelSerializer):
    application = ApplicationsListSerializer()
    state_duty_score = StateDutyScoreDetailSerializer()
    state_duty_percent = StateDutyPercentDetailShortSerializer()

    class Meta:
        model = PaymentForTreasury
        fields = [
            'id',
            'application',
            'amount',
            'state_duty_score',
            'state_duty_percent',
            'amount_base_calculation',
            'memorial',
            'transaction_id',
            'status',
            'created_at'
        ]

    def to_representation(self, instance):
        context = super(PaymentForTreasuryListSerializer, self).to_representation(instance)
        if instance.application.applicant:
            context['applicant'] = UserShortDetailSerializer(instance.application.applicant).data
        else:
            context['applicant'] = UserShortDetailSerializer(instance.application.created_user).data

        if instance.application.applicant:
            context['district'] = DistrictDetailSerializer(instance.application.applicant.district).data
        else:
            context['district'] = DistrictDetailSerializer(instance.application.created_user.district).data
        return context