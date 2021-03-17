import json
import random

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from application.models import *
from service.models import StateDutyPercent
from service.utils import calculation_state_duty_service_price
from user.models import *


@login_required
def account_statement_index(request):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    # get previous years
    year = datetime.datetime.today().year
    years = range(year, year - 80, -1)
    cars = CarModel.objects.all()
    fuel_types = FuelType.objects.filter(is_active=True)
    car_types = CarType.objects.filter(is_active=True)
    devices = Device.objects.filter(is_active=True)
    bodyTypes = BodyType.objects.filter(is_active=True)
    colors = Color.objects.filter(is_active=True)
    organizations = Organization.objects.filter(created_user=request.user, is_active=True)
    services = StateDutyPercent.objects.filter(service='account_statement')

    context = {
        'cars': cars,
        'organizations': organizations,
        'fuel_types': fuel_types,
        'car_types': car_types,
        'devices': devices,
        'bodyTypes': bodyTypes,
        'years': years,
        'color': colors,
        'services': services
    }
    return render(request, 'service/account_statement/account_statement_index.html', context=context)

@permission_classes([IsAuthenticated])
class Save_Account_Statement(APIView):
    def post(self, request):
        print(request.POST)
        if request.is_ajax():
            person_type = request.POST.get('person_type')
            engine_number = request.POST.get('engine_number')
            full_weight = request.POST.get('full_weight')
            empty_weight = request.POST.get('empty_weight')
            engine_power = request.POST.get('engine_power')
            auction_number = request.POST.get('auction_number')
            body_number = request.POST.get('body_number')
            color = get_object_or_404(Color, id=request.POST.get('color', None))
            made_year = request.POST.get('made_year')
            devices = []
            if request.POST.getlist('devices'):
                for device_id in list(filter(None, request.POST.getlist('devices'))):
                    devices.append(get_object_or_404(Device, id=device_id))

            fuel_types = []
            if request.POST.getlist('fuel_types'):
                for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                    fuel_types.append(get_object_or_404(FuelType, id=fuel_type_id))

            seriya = request.POST.get('account_statement')
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
            car.empty_weight = empty_weight
            car.engine_power = engine_power
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
            service = Service.objects.create(person_type=person_type, car=car, title='account_statement', contract_date=contract_date)
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
def gift_agreement_index(request):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    # get previous years
    year = datetime.datetime.today().year
    years = range(year, year - 80, -1)
    cars = CarModel.objects.all()
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
        'years': years,
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

            old_number = request.POST.get('old_number')
            body_number = request.POST.get('body_number')
            color = get_object_or_404(Color, id=request.POST.get('color', None))
            made_year = request.POST.get('made_year')
            devices = []
            if request.POST.getlist('devices'):
                for device_id in list(filter(None, request.POST.getlist('devices'))):
                    devices.append(get_object_or_404(Device, id=device_id))

            fuel_types = []
            if request.POST.getlist('fuel_types'):
                for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                    fuel_types.append(get_object_or_404(FuelType, id=fuel_type_id))

            seriya = request.POST.get('gift_agreement')
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
    year = datetime.datetime.today().year
    years = range(year, year - 80, -1)
    cars = CarModel.objects.all()
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
        'years': years,
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

            old_number = request.POST.get('old_number')
            body_number = request.POST.get('body_number')
            color = get_object_or_404(Color, id=request.POST.get('color', None))
            made_year = request.POST.get('made_year')
            devices = []
            if request.POST.getlist('devices'):
                for device_id in list(filter(None, request.POST.getlist('devices'))):
                    devices.append(get_object_or_404(Device, id=device_id))

            fuel_types = []
            if request.POST.getlist('fuel_types'):
                for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                    fuel_types.append(get_object_or_404(FuelType, id=fuel_type_id))

            seriya = request.POST.get('contract_of_sale')
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
                'html': calculation_state_duty_service_price(service),
                'application': application.file_name
            }

            data = json.dumps(context)
            return HttpResponse(data, content_type='json')
        else:
            return HttpResponse(False)