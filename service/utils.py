from django.core.exceptions import ObjectDoesNotExist

from user.models import Constant


def calculation_state_duty_service_price(obj):
    try:
        MINIMUM_BASE_WAGE = int(Constant.objects.get(key='MINIMUM_BASE_WAGE').value)
        price = MINIMUM_BASE_WAGE / 100 * obj.percent
        return int(price)
    except ObjectDoesNotExist:
        return 'ERROR OBJECT NOT FOUND'