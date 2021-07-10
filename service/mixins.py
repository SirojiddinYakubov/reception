from django.views.generic import ListView

from reception.mixins import *
from reception.settings import *
from service.models import *
from user.models import *


class ServiceCustomMixin(AllowedRolesMixin, ListView):
    model = Service
    allowed_roles = [USER, CHECKER, REVIEWER, TECHNICAL, DISTRICAL_CONTROLLER, REGIONAL_CONTROLLER, STATE_CONTROLLER, MODERATOR, ADMINISTRATOR, SUPER_ADMINISTRATOR]

    def get_context_data(self, **kwargs):
        cars = CarModel.objects.filter(is_active=True)
        fuel_types = FuelType.objects.filter(is_active=True)
        car_types = CarType.objects.filter(is_active=True)
        devices = Device.objects.filter(is_active=True)
        bodyTypes = BodyType.objects.filter(is_active=True)
        colors = Color.objects.filter(is_active=True)
        organizations = Organization.objects.filter(created_user=self.request.user, is_active=True)

        context = {
            'cars': cars,
            'organizations': organizations,
            'fuel_types': fuel_types,
            'car_types': car_types,
            'devices': devices,
            'bodyTypes': bodyTypes,
            'color': colors,
            'PAY_FOR_SERVICE': PAY_FOR_SERVICE,
            'PAY_FOR_SERVICE_PERCENT': PAY_FOR_SERVICE_PERCENT
        }
        return context