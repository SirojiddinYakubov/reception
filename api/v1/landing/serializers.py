from rest_framework import serializers, exceptions

# from landing.models import
from application.models import PERSON_CHOICES
from service.models import (Service)
from user.models import (CarType)


class CalculateSerializer(serializers.Serializer):
    service = serializers.PrimaryKeyRelatedField(required=True, queryset=Service.objects.all())
    type = serializers.PrimaryKeyRelatedField(required=True, queryset=CarType.objects.all())
    is_local = serializers.BooleanField()
    person_type = serializers.ChoiceField(required=True, choices=PERSON_CHOICES)
    engine_power = serializers.CharField(required=False)
    price = serializers.CharField(required=False)
    made_year = serializers.DateField(required=False)
    contract_date = serializers.DateField(required=False)
    is_auction = serializers.BooleanField()
    save_old_number = serializers.BooleanField()
    is_saved_number = serializers.BooleanField()
    lost_number = serializers.BooleanField()
    is_old_number = serializers.BooleanField()
    lost_technical_passport = serializers.BooleanField()
    is_relative = serializers.BooleanField()

    def validate(self, attrs):
        if attrs['service']:
            service = attrs['service']

            if service.key == 'account_statement':
                if not attrs.get('price'):
                    raise serializers.ValidationError('price required field')
                if not attrs.get('contract_date'):
                    raise serializers.ValidationError('contract_date required field')
                if not attrs.get('made_year'):
                    raise serializers.ValidationError('made_year required field')
            if service.key == 'contract_of_sale':
                if not attrs.get('contract_date'):
                    raise serializers.ValidationError('contract_date required field')
                if not attrs.get('made_year'):
                    raise serializers.ValidationError('made_year required field')
                if not attrs.get('engine_power'):
                    raise serializers.ValidationError('engine_power required field')
            if service.key == 'gift_agreement' or service.key == 'inheritance_agreement':
                if not attrs.get('contract_date'):
                    raise serializers.ValidationError('contract_date required field')
        return attrs