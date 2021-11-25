from rest_framework import serializers

from api.v1.user.serializers import CarTypesListSerializer
from service.models import (
    Service, StateDutyPercent, AmountBaseCalculation, ROAD_FUND, ROAD_FUND_HORSE_POWER, STATE_DUTY_TITLE
)


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'short_title',
            'long_title',
            'key',
        ]


class ServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = [
            'id',
            'short_title',
            'long_title',
            'key',
            'is_active',
            'desc',
            'photo',
            'deadline',
            'instruction',
            'document',
            'created_date',
            'sort',
        ]


class StateDutyPercentDetailSerializer(serializers.ModelSerializer):
    # service = ServiceListSerializer(many=True)
    # car_type = CarTypesListSerializer(many=True)

    class Meta:
        model = StateDutyPercent
        fields = [
            'id',
            'title',
            'service',
            'state_duty',
            'person_type',
            'car_type',
            'car_is_new',
            'is_old_number',
            'is_save_old_number',
            'lost_number',
            'lost_technical_passport',
            'is_auction',
            'is_tranzit',
            'start',
            'stop',
            'percent',
        ]

    def to_representation(self, instance):
        context = super().to_representation(instance)
        engine_power = self.context['engine_power']
        price = self.context['price']

        try:
            amount_base_calculation = AmountBaseCalculation.objects.get(is_active=True)
            if instance.state_duty == ROAD_FUND:
                payment = round(round(instance.percent, 2) / 100 * round(int(price), 2), 2)
            elif instance.state_duty == ROAD_FUND_HORSE_POWER:
                payment = round(amount_base_calculation.amount / 100 * round(instance.percent, 2) * int(engine_power),
                                2)
            else:
                payment = amount_base_calculation.amount / 100 * round(instance.percent, 2)
            context['amount'] = round(payment, 2)
        except Exception as e:
            print(e)
            context['amount'] = instance.percent
        context['state_duty'] = dict(STATE_DUTY_TITLE).get(context['state_duty'])
        return context
