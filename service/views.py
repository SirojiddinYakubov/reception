import json
import random

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from application.models import *
from reception.mixins import AllowedRolesMixin
from reception.settings import *
from service.mixins import ServiceCustomMixin
from service.models import StateDutyPercent, StateDuty, STATE_DUTY_TITLE
from service.utils import calculation_state_duty_service_price
from user.models import *


class AccountStatement(ServiceCustomMixin):
    template_name = 'service/account_statement/account_statement.html'

    def post(self, request, *args, **kwargs):
        return self.get_json_data()

    def get_json_data(self):

        try:
            request = self.request
            print(request.POST)
            person_type = request.POST.get('person_type')
            engine_number = request.POST.get('engine_number')
            full_weight = request.POST.get('full_weight')
            empty_weight = request.POST.get('empty_weight')
            engine_power = request.POST.get('engine_power')
            auction_number = request.POST.get('auction_number')
            body_number = request.POST.get('body_number')
            price = request.POST.get('price')
            color = get_object_or_404(Color, id=request.POST.get('color', None))
            made_year = datetime.datetime.strptime(request.POST.get('made_year', None), '%Y-%m-%d')

            devices = []
            if request.POST.getlist('devices'):
                for device_id in list(filter(None, request.POST.getlist('devices'))):
                    devices.append(get_object_or_404(Device, id=device_id))

            fuel_types = []
            if request.POST.getlist('fuel_types'):
                for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                    fuel_types.append(get_object_or_404(FuelType, id=fuel_type_id))

            seriya = request.POST.get('seriya')
            if request.POST.get('contract_date', None):
                contract_date = datetime.datetime.strptime(request.POST.get('contract_date'), '%Y-%m-%d')
            user = get_object_or_404(User, id=request.user.id)
            get_car = get_object_or_404(CarModel, id=request.POST.get('car'))

            # create car
            car = Car.objects.create(model=get_car)
            car.body_type = get_object_or_404(BodyType, id=request.POST.get('body_type', None))
            if request.POST.get('chassis_number', None):
                car.chassis_number = request.POST.get('chassis_number', None)
            car.body_number = body_number
            car.engine_number = engine_number
            car.type = get_object_or_404(CarType, id=request.POST.get('car_type'))
            car.made_year = made_year
            car.full_weight = full_weight
            car.empty_weight = empty_weight
            car.engine_power = engine_power
            car.is_new = True
            car.is_replace_number = True
            if get_car.is_local:
                if car.made_year < datetime.datetime.strptime('25.12.2020', '%d.%m.%Y'):
                    car.is_road_fund = True
                else:
                    car.is_road_fund = False
            else:
                car.is_road_fund = True

            car.price = price
            if request.POST.get('auction_number'):
                car.is_auction = True
                car.given_number = auction_number
            car.color = color
            for fuel_type in fuel_types:
                car.fuel_type.add(fuel_type)
            for device in devices:
                car.device.add(device)
            car.save()

            # create application and account_statament
            application = Application.objects.create(created_user=user, created_date=timezone.now())
            if person_type == LEGAL_PERSON:
                organization = get_object_or_404(Organization, id=request.POST.get('organization'))
                application.person_type = person_type
                application.organization = organization
            application.save()

            password = random.randint(1000, 9999)
            application.password = password
            service = get_object_or_404(Service, key='account_statement')
            application.service = service
            application.car = car
            application.save()



            # calculation_state_duty_service_price(service)
            #
            # stateDuties = list()
            # stateDuties.append({'application': application.file_name})
            # qs = StateDuty.objects.filter(service=service)
            # print(qs)
            # for query in qs:
            #     stateDuties.append({'title':query.get_title_display(), 'payment':query.payment})

            # print(stateDuties)
            context = {
                # 'stateDuties': serializers.serialize('json', stateDuties),
                # 'application': application.file_name
            }
            obj_serialize = serializers.serialize('json', [application,])
            # data = json.dumps(obj_serialize)
            return HttpResponse(application.id, content_type='json', status=200)
        except:
            return HttpResponse(status=400)

@login_required
def gift_agreement_index(request):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    cars = CarModel.objects.filter(is_active=True)
    fuel_types = FuelType.objects.filter(is_active=True)
    car_types = CarType.objects.filter(is_active=True)
    devices = Device.objects.filter(is_active=True)
    bodyTypes = BodyType.objects.filter(is_active=True)
    colors = Color.objects.filter(is_active=True)
    organizations = Organization.objects.filter(created_user=request.user, is_active=True)

    context = {
        'cars': cars,
        'organizations': organizations,
        'fuel_types': fuel_types,
        'car_types': car_types,
        'devices': devices,
        'bodyTypes': bodyTypes,
        'color': colors,

    }
    return render(request, 'service/gift_agreement/gift_agreement_index.html', context)


@permission_classes([IsAuthenticated])
class Save_Gift_Agreement(APIView):
    def post(self, request):
        print(request.POST)
        if request.is_ajax():
            person_type = request.POST.get('person_type')
            engine_number = request.POST.get('engine_number')
            full_weight = request.POST.get('full_weight')
            empty_weight = request.POST.get('empty_weight')
            engine_power = request.POST.get('engine_power')
            auction_number = request.POST.get('auction_number')
            old_technical_passport = request.POST.get('old_technical_passport')

            if request.POST.get('lost_technical_passport') == 'on':
                lost_technical_passport = True
            else:
                lost_technical_passport = False

            if request.POST.get('lost_number') == 'on':
                lost_number = True
            else:
                lost_number = False

            if request.POST.get('is_old_number') == 'on':
                is_old_number = True
            else:
                is_old_number = False

            old_number = request.POST.get('old_number')
            body_number = request.POST.get('body_number')
            color = get_object_or_404(Color, id=request.POST.get('color', None))
            made_year = datetime.datetime.strptime(request.POST.get('made_year', None),'%d.%m.%Y')
            devices = []
            if request.POST.getlist('devices'):
                for device_id in list(filter(None, request.POST.getlist('devices'))):
                    devices.append(get_object_or_404(Device, id=device_id))

            fuel_types = []
            if request.POST.getlist('fuel_types'):
                for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                    fuel_types.append(get_object_or_404(FuelType, id=fuel_type_id))

            seriya = request.POST.get('seriya')
            contract_date = datetime.datetime.strptime(request.POST.get('contract_date', None),'%d.%m.%Y')
            user = get_object_or_404(User, id=request.user.id)
            get_car = get_object_or_404(CarModel, id=request.POST.get('car'))

            # create car
            car = Car.objects.create(model=get_car)
            car.body_type = get_object_or_404(BodyType, id=request.POST.get('body_type', None))
            if request.POST.get('chassis_number', None):
                car.chassis_number = request.POST.get('chassis_number', None)
            car.body_number = body_number
            car.engine_number = engine_number
            car.type = get_object_or_404(CarType, id=request.POST.get('car_type'))
            car.made_year = made_year
            car.full_weight = full_weight
            car.old_number = old_number
            car.old_technical_passport = old_technical_passport
            car.lost_technical_passport = lost_technical_passport
            car.empty_weight = empty_weight
            car.engine_power = engine_power
            car.lost_number = lost_number
            car.is_old_number = is_old_number
            car.is_replace_number = True
            car.is_road_fund = False
            # if get_car.is_local:
            #     if car.made_year < datetime.datetime.strptime('25.12.2020', '%d.%m.%Y'):
            #         car.is_road_fund = True
            #     else:
            #         car.is_road_fund = False
            # else:
            #     car.is_road_fund = True

            if request.POST.get('auction_number'):
                car.is_auction = True
                car.given_number = auction_number
            car.color = color
            for fuel_type in fuel_types:
                car.fuel_type.add(fuel_type)
            for device in devices:
                car.device.add(device)
            car.save()

            # create application and account_statament
            application = Application.objects.create(created_user=user, created_date=timezone.now())
            service = Service.objects.create(person_type=person_type, car=car, title='gift_agreement', contract_date=contract_date)
            service.seriya = seriya
            service.created_user = request.user
            if person_type == 'Y':
                organization = get_object_or_404(Organization, id=request.POST.get('organization'))
                application.person_type = person_type
                service.organization = organization
            service.save()

            password = random.randint(1000, 9999)
            application.password = password
            application.service = service
            application.save()

            context = {
                'html': calculation_state_duty_service_price(service),
                'application': application.file_name
            }

            data = json.dumps(context)
            return HttpResponse(data, content_type='json')
        else:
            return HttpResponse(False)


@login_required
def contract_of_sale_index(request):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    # get previous years
    # year = datetime.datetime.today().year
    # years = range(year, year - 80, -1)
    cars = CarModel.objects.filter(is_active=True)
    fuel_types = FuelType.objects.filter(is_active=True)
    car_types = CarType.objects.filter(is_active=True)
    devices = Device.objects.filter(is_active=True)
    bodyTypes = BodyType.objects.filter(is_active=True)
    colors = Color.objects.filter(is_active=True)
    organizations = Organization.objects.filter(created_user=request.user, is_active=True)

    context = {
        'cars': cars,
        'organizations': organizations,
        'fuel_types': fuel_types,
        'car_types': car_types,
        'devices': devices,
        'bodyTypes': bodyTypes,
        'color': colors,

    }
    return render(request, 'service/contract_of_sale/contract_of_sale_index.html', context)


@permission_classes([IsAuthenticated])
class Save_Contract_Of_Sale(APIView):
    def post(self, request):
        print(request.POST)
        if request.is_ajax():
            person_type = request.POST.get('person_type')
            engine_number = request.POST.get('engine_number')
            full_weight = request.POST.get('full_weight')
            empty_weight = request.POST.get('empty_weight')
            engine_power = request.POST.get('engine_power')
            auction_number = request.POST.get('auction_number')
            old_technical_passport = request.POST.get('old_technical_passport')

            if request.POST.get('lost_technical_passport') == 'on':
                lost_technical_passport = True
            else:
                lost_technical_passport = False

            if request.POST.get('lost_number') == 'on':
                lost_number = True
            else:
                lost_number = False

            if request.POST.get('is_old_number') == 'on':
                is_old_number = True
            else:
                is_old_number = False

            old_number = request.POST.get('old_number')
            body_number = request.POST.get('body_number')
            color = get_object_or_404(Color, id=request.POST.get('color', None))
            made_year = datetime.datetime.strptime(request.POST.get('made_year', None),'%d.%m.%Y')
            devices = []
            if request.POST.getlist('devices'):
                for device_id in list(filter(None, request.POST.getlist('devices'))):
                    devices.append(get_object_or_404(Device, id=device_id))

            fuel_types = []
            if request.POST.getlist('fuel_types'):
                for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                    fuel_types.append(get_object_or_404(FuelType, id=fuel_type_id))

            seriya = request.POST.get('seriya')
            contract_date = datetime.datetime.strptime(request.POST.get('contract_date', None),'%d.%m.%Y')
            user = get_object_or_404(User, id=request.user.id)
            get_car = get_object_or_404(CarModel, id=request.POST.get('car'))

            # create car
            car = Car.objects.create(model=get_car)
            car.body_type = get_object_or_404(BodyType, id=request.POST.get('body_type', None))
            if request.POST.get('chassis_number', None):
                car.chassis_number = request.POST.get('chassis_number', None)
            car.body_number = body_number
            car.engine_number = engine_number
            car.type = get_object_or_404(CarType, id=request.POST.get('car_type'))
            car.made_year = made_year
            car.full_weight = full_weight
            car.old_number = old_number
            car.old_technical_passport = old_technical_passport
            car.lost_technical_passport = lost_technical_passport
            car.empty_weight = empty_weight
            car.engine_power = engine_power
            car.lost_number = lost_number
            car.is_old_number = is_old_number
            car.is_replace_number = True
            if get_car.is_local:
                if car.made_year < datetime.datetime.strptime('25.12.2020', '%d.%m.%Y'):
                    car.is_road_fund = True
                else:
                    car.is_road_fund = False
            else:
                car.is_road_fund = True

            if request.POST.get('auction_number'):
                car.is_auction = True
                car.given_number = auction_number
            car.color = color
            for fuel_type in fuel_types:
                car.fuel_type.add(fuel_type)
            for device in devices:
                car.device.add(device)
            car.save()

            # create application and account_statament
            application = Application.objects.create(created_user=user, created_date=timezone.now())
            service = Service.objects.create(person_type=person_type, car=car, title='contract_of_sale', contract_date=contract_date)
            service.seriya = seriya
            service.created_user = request.user
            if person_type == 'Y':
                organization = get_object_or_404(Organization, id=request.POST.get('organization'))
                application.person_type = person_type
                service.organization = organization
            service.save()

            password = random.randint(1000, 9999)
            application.password = password
            application.service = service
            application.save()

            # app = serializers.serialize('json', [application, ])
            # struct = json.loads(app)
            # data = json.dumps(struct[0])
            # return HttpResponse(data, content_type='json')

            context = {
                'application': application.file_name
            }

            data = json.dumps(context)
            return HttpResponse(data, content_type='json')
        else:
            return HttpResponse(False)


@login_required
def replace_tp_index(request):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    cars = CarModel.objects.filter(is_active=True)
    fuel_types = FuelType.objects.filter(is_active=True)
    car_types = CarType.objects.filter(is_active=True)
    devices = Device.objects.filter(is_active=True)
    bodyTypes = BodyType.objects.filter(is_active=True)
    colors = Color.objects.filter(is_active=True)
    organizations = Organization.objects.filter(created_user=request.user, is_active=True)

    context = {
        'cars': cars,
        'organizations': organizations,
        'fuel_types': fuel_types,
        'car_types': car_types,
        'devices': devices,
        'bodyTypes': bodyTypes,
        'color': colors,

    }
    return render(request, 'service/replace_tp/replace_tp_index.html', context)


@permission_classes([IsAuthenticated])
class Save_Replace_Tp(APIView):
    def post(self, request):
        print(request.POST)
        if request.is_ajax():
            person_type = request.POST.get('person_type')
            engine_number = request.POST.get('engine_number')
            full_weight = request.POST.get('full_weight')
            empty_weight = request.POST.get('empty_weight')
            engine_power = request.POST.get('engine_power')
            old_technical_passport = request.POST.get('old_technical_passport')

            if request.POST.get('lost_technical_passport') == 'on':
                lost_technical_passport = True
            else:
                lost_technical_passport = False


            old_number = request.POST.get('old_number')
            body_number = request.POST.get('body_number')
            color = get_object_or_404(Color, id=request.POST.get('color', None))
            made_year = datetime.datetime.strptime(request.POST.get('made_year', None),'%d.%m.%Y')
            devices = []
            if request.POST.getlist('devices'):
                for device_id in list(filter(None, request.POST.getlist('devices'))):
                    devices.append(get_object_or_404(Device, id=device_id))

            fuel_types = []
            if request.POST.getlist('fuel_types'):
                for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                    fuel_types.append(get_object_or_404(FuelType, id=fuel_type_id))

            user = get_object_or_404(User, id=request.user.id)
            get_car = get_object_or_404(CarModel, id=request.POST.get('car'))

            # create car
            car = Car.objects.create(model=get_car)
            car.body_type = get_object_or_404(BodyType, id=request.POST.get('body_type', None))
            if request.POST.get('chassis_number', None):
                car.chassis_number = request.POST.get('chassis_number', None)
            car.body_number = body_number
            car.engine_number = engine_number
            car.type = get_object_or_404(CarType, id=request.POST.get('car_type'))
            car.made_year = made_year
            car.full_weight = full_weight
            car.old_number = old_number
            car.old_technical_passport = old_technical_passport
            car.lost_technical_passport = lost_technical_passport
            car.empty_weight = empty_weight
            car.engine_power = engine_power
            car.is_replace_number = False
            car.is_road_fund = False
            car.color = color
            for fuel_type in fuel_types:
                car.fuel_type.add(fuel_type)
            for device in devices:
                car.device.add(device)
            car.save()

            # create application and account_statament
            application = Application.objects.create(created_user=user, created_date=timezone.now())
            service = Service.objects.create(person_type=person_type, car=car, title='replace_tp')
            service.created_user = request.user
            if person_type == 'Y':
                organization = get_object_or_404(Organization, id=request.POST.get('organization'))
                application.person_type = person_type
                service.organization = organization
            service.save()

            password = random.randint(1000, 9999)
            application.password = password
            application.service = service
            application.save()

            # app = serializers.serialize('json', [application, ])
            # struct = json.loads(app)
            # data = json.dumps(struct[0])
            # return HttpResponse(data, content_type='json')
            context = {
                'html': calculation_state_duty_service_price(service),
                'application': application.file_name
            }

            data = json.dumps(context)
            return HttpResponse(data, content_type='json')
        else:
            return HttpResponse(False)


@login_required
def replace_number_and_tp_index(request):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    cars = CarModel.objects.filter(is_active=True)
    fuel_types = FuelType.objects.filter(is_active=True)
    car_types = CarType.objects.filter(is_active=True)
    devices = Device.objects.filter(is_active=True)
    bodyTypes = BodyType.objects.filter(is_active=True)
    colors = Color.objects.filter(is_active=True)
    organizations = Organization.objects.filter(created_user=request.user, is_active=True)

    context = {
        'cars': cars,
        'organizations': organizations,
        'fuel_types': fuel_types,
        'car_types': car_types,
        'devices': devices,
        'bodyTypes': bodyTypes,
        'color': colors,

    }
    return render(request, 'service/replace_number_and_tp/replace_number_and_tp_index.html', context)


@permission_classes([IsAuthenticated])
class Save_Replace_Number_And_Tp(APIView):
    def post(self, request):
        print(request.POST)
        if request.is_ajax():
            person_type = request.POST.get('person_type')
            engine_number = request.POST.get('engine_number')
            full_weight = request.POST.get('full_weight')
            empty_weight = request.POST.get('empty_weight')
            engine_power = request.POST.get('engine_power')
            auction_number = request.POST.get('auction_number')
            old_technical_passport = request.POST.get('old_technical_passport')

            if request.POST.get('lost_technical_passport') == 'on':
                lost_technical_passport = True
            else:
                lost_technical_passport = False

            if request.POST.get('lost_number') == 'on':
                lost_number = True
            else:
                lost_number = False

            if request.POST.get('is_old_number') == 'on':
                is_old_number = True
            else:
                is_old_number = False

            old_number = request.POST.get('old_number')
            body_number = request.POST.get('body_number')
            color = get_object_or_404(Color, id=request.POST.get('color', None))
            made_year = datetime.datetime.strptime(request.POST.get('made_year', None),'%d.%m.%Y')
            devices = []
            if request.POST.getlist('devices'):
                for device_id in list(filter(None, request.POST.getlist('devices'))):
                    devices.append(get_object_or_404(Device, id=device_id))

            fuel_types = []
            if request.POST.getlist('fuel_types'):
                for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                    fuel_types.append(get_object_or_404(FuelType, id=fuel_type_id))


            user = get_object_or_404(User, id=request.user.id)
            get_car = get_object_or_404(CarModel, id=request.POST.get('car'))

            # create car
            car = Car.objects.create(model=get_car)
            car.body_type = get_object_or_404(BodyType, id=request.POST.get('body_type', None))
            if request.POST.get('chassis_number', None):
                car.chassis_number = request.POST.get('chassis_number', None)
            car.body_number = body_number
            car.engine_number = engine_number
            car.type = get_object_or_404(CarType, id=request.POST.get('car_type'))
            car.made_year = made_year
            car.full_weight = full_weight
            car.old_number = old_number
            car.old_technical_passport = old_technical_passport
            car.lost_technical_passport = lost_technical_passport
            car.empty_weight = empty_weight
            car.engine_power = engine_power
            car.lost_number = lost_number
            car.is_old_number = is_old_number
            car.is_replace_number = True
            car.is_road_fund = False
            if request.POST.get('auction_number'):
                car.is_auction = True
                car.given_number = auction_number
            car.color = color
            for fuel_type in fuel_types:
                car.fuel_type.add(fuel_type)
            for device in devices:
                car.device.add(device)
            car.save()

            # create application and account_statament
            application = Application.objects.create(created_user=user, created_date=timezone.now())
            service = Service.objects.create(person_type=person_type, car=car, title='replace_number_and_tp')

            service.created_user = request.user
            if person_type == 'Y':
                organization = get_object_or_404(Organization, id=request.POST.get('organization'))
                application.person_type = person_type
                service.organization = organization
            service.save()

            password = random.randint(1000, 9999)
            application.password = password
            application.service = service
            application.save()

            # app = serializers.serialize('json', [application, ])
            # struct = json.loads(app)
            # data = json.dumps(struct[0])
            # return HttpResponse(data, content_type='json')
            context = {
                'html': calculation_state_duty_service_price(service),
                'application': application.file_name
            }

            data = json.dumps(context)
            return HttpResponse(data, content_type='json')
        else:
            return HttpResponse(False)


@login_required
def re_equipment_index(request):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    cars = CarModel.objects.filter(is_active=True)
    fuel_types = FuelType.objects.filter(is_active=True)
    car_types = CarType.objects.filter(is_active=True)
    devices = Device.objects.filter(is_active=True)
    bodyTypes = BodyType.objects.filter(is_active=True)
    colors = Color.objects.filter(is_active=True)
    organizations = Organization.objects.filter(created_user=request.user, is_active=True)

    context = {
        'cars': cars,
        'organizations': organizations,
        'fuel_types': fuel_types,
        'car_types': car_types,
        'devices': devices,
        'bodyTypes': bodyTypes,
        'color': colors,

    }
    return render(request, 'service/re_equipment/re_equipment_index.html', context)


@permission_classes([IsAuthenticated])
class Save_Re_Equipment(APIView):
    def post(self, request):
        print(request.POST)
        if request.is_ajax():
            person_type = request.POST.get('person_type')
            engine_number = request.POST.get('engine_number')
            full_weight = request.POST.get('full_weight')
            empty_weight = request.POST.get('empty_weight')
            engine_power = request.POST.get('engine_power')
            old_technical_passport = request.POST.get('old_technical_passport')

            if request.POST.get('lost_technical_passport') == 'on':
                lost_technical_passport = True
            else:
                lost_technical_passport = False


            old_number = request.POST.get('old_number')
            body_number = request.POST.get('body_number')
            color = get_object_or_404(Color, id=request.POST.get('color', None))
            if request.POST.get('re_color'):
                re_color = get_object_or_404(Color, id=request.POST.get('re_color', None))
            else:
                re_color = None
            made_year = datetime.datetime.strptime(request.POST.get('made_year', None),'%d.%m.%Y')
            devices = []
            if request.POST.getlist('devices'):
                for device_id in list(filter(None, request.POST.getlist('devices'))):
                    devices.append(get_object_or_404(Device, id=device_id))

            fuel_types = []
            if request.POST.getlist('fuel_types'):
                for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                    fuel_types.append(get_object_or_404(FuelType, id=fuel_type_id))

            re_fuel_types = []
            if request.POST.getlist('re_fuel_types'):
                for re_fuel_type_id in list(filter(None, request.POST.getlist('re_fuel_types'))):
                    re_fuel_types.append(get_object_or_404(FuelType, id=re_fuel_type_id))

            user = get_object_or_404(User, id=request.user.id)
            get_car = get_object_or_404(CarModel, id=request.POST.get('car'))

            # create car
            car = Car.objects.create(model=get_car)
            car.body_type = get_object_or_404(BodyType, id=request.POST.get('body_type', None))
            if request.POST.get('chassis_number', None):
                car.chassis_number = request.POST.get('chassis_number', None)
            car.body_number = body_number
            car.engine_number = engine_number
            car.type = get_object_or_404(CarType, id=request.POST.get('car_type'))
            car.made_year = made_year
            car.full_weight = full_weight
            car.old_number = old_number
            car.old_technical_passport = old_technical_passport
            car.lost_technical_passport = lost_technical_passport
            car.empty_weight = empty_weight
            car.engine_power = engine_power
            car.is_replace_number = False
            car.is_road_fund = False
            car.color = color
            car.re_color = re_color
            for fuel_type in fuel_types:
                car.fuel_type.add(fuel_type)
            for re_fuel_type in re_fuel_types:
                car.re_fuel_type.add(re_fuel_type)
            for device in devices:
                car.device.add(device)
            car.save()

            # create application and account_statament
            application = Application.objects.create(created_user=user, created_date=timezone.now())
            service = Service.objects.create(person_type=person_type, car=car, title='re_equipment')
            service.created_user = request.user
            if person_type == 'Y':
                organization = get_object_or_404(Organization, id=request.POST.get('organization'))
                application.person_type = person_type
                service.organization = organization
            service.save()

            password = random.randint(1000, 9999)
            application.password = password
            application.service = service
            application.save()

            # app = serializers.serialize('json', [application, ])
            # struct = json.loads(app)
            # data = json.dumps(struct[0])
            # return HttpResponse(data, content_type='json')
            context = {
                'html': calculation_state_duty_service_price(service),
                'application': application.file_name
            }

            data = json.dumps(context)
            return HttpResponse(data, content_type='json')
        else:
            return HttpResponse(False)


class ServicesList(ListView):
    model = Service
    template_name = 'services/services_list.html'
    ordering = ['id']

    context_object_name = 'services'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        qs = super().get_queryset().filter(is_active=True)
        return qs


class ServiceInfo(DetailView):
    model = Service
    template_name = 'services/service_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context.update(form_fields=ServiceInputField.objects.filter(service=self.kwargs.get('pk')))
        return context


