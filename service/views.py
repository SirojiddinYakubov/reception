import datetime
import json
import random

from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from application.models import *
from reception.api import SendSmsWithPlayMobile
from service.mixins import ServiceCustomMixin
from user.models import *


class AccountStatement(ServiceCustomMixin):
    template_name = 'service/account_statement/account_statement.html'

    def get_template_names(self):
        role = self.request.user.role
        print(role)
        if role == APP_CREATOR:
            print('ok')
            return ['user/role/app_creator/service/account_statement.html']
        else:
            return [self.template_name]

    def get(self, request, *args, **kwargs):
        return super().get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.get_json_data()

    def get_json_data(self):
        try:
            with transaction.atomic():
                request = self.request
                print(request.POST)
                service = Service.objects.get(key='account_statement')
                person_type = request.POST.get('person_type')
                engine_number = request.POST.get('engine_number')
                full_weight = request.POST.get('full_weight')
                empty_weight = request.POST.get('empty_weight')
                engine_power = request.POST.get('engine_power')
                auction_number = request.POST.get('auction_number')
                body_number = request.POST.get('body_number')
                price = request.POST.get('price')
                color = Color.objects.get(id=request.POST.get('color', None))
                made_year = datetime.datetime.strptime(request.POST.get('made_year', None), '%Y-%m-%d')
                devices = []
                if request.POST.getlist('devices'):
                    for device_id in list(filter(None, request.POST.getlist('devices'))):
                        devices.append(Device.objects.get(id=device_id))

                fuel_types = []
                if request.POST.getlist('fuel_types'):
                    for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                        fuel_types.append(FuelType.objects.get(id=fuel_type_id))

                user = User.objects.get(id=request.user.id)

                get_car = CarModel.objects.get(id=request.POST.get('car'))

                # create car
                car = Car.objects.create(model=get_car)
                car.body_type = BodyType.objects.get(id=request.POST.get('body_type', None))

                if request.POST.get('chassis_number', None):
                    car.chassis_number = request.POST.get('chassis_number', None)
                car.body_number = body_number
                car.engine_number = engine_number
                car.type = CarType.objects.get(id=request.POST.get('car_type'))
                car.made_year = made_year
                car.full_weight = full_weight
                car.empty_weight = empty_weight
                car.engine_power = engine_power

                car.is_new = True
                car.is_replace_number = True

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

                if int(person_type) == LEGAL_PERSON:

                    organization = Organization.objects.get(id=request.POST.get('organization'))

                    application.person_type = person_type
                    application.organization = organization

                password = random.randint(1000, 9999)
                application.password = password
                application.service = service
                application.car = car
                if request.POST.get('seriya', None) and request.POST.get('contract_date', None):
                    seriya = request.POST.get('seriya')
                    contract_date = datetime.datetime.strptime(request.POST.get('contract_date'), '%Y-%m-%d')
                example_document = ExampleDocument.objects.get(key=service.key)
                application_document = ApplicationDocument.objects.filter(application=application,
                                                                          example_document=example_document)
                if not application_document.exists():
                    ApplicationDocument.objects.create(application=application,
                                                       example_document=example_document,
                                                       seriya=seriya,
                                                       contract_date=contract_date)
                application.save()

                return HttpResponse(application.id, content_type='json', status=200)
        except Exception as e:
            print(e)
            return HttpResponse(e, status=400)


class ContractOfSale(ServiceCustomMixin):
    template_name = 'service/contract_of_sale/contract_of_sale.html'

    def post(self, request, *args, **kwargs):
        return self.get_json_data()

    def get_json_data(self):
        try:
            with transaction.atomic():
                request = self.request
                service = Service.objects.get(key='contract_of_sale')

                person_type = request.POST.get('person_type')
                engine_number = request.POST.get('engine_number')
                full_weight = request.POST.get('full_weight')
                empty_weight = request.POST.get('empty_weight')
                engine_power = request.POST.get('engine_power')
                body_number = request.POST.get('body_number')

                color = Color.objects.get(id=request.POST.get('color', None))
                made_year = datetime.datetime.strptime(request.POST.get('made_year', None), '%Y-%m-%d')

                devices = []
                if request.POST.getlist('devices'):
                    for device_id in list(filter(None, request.POST.getlist('devices'))):
                        devices.append(Device.objects.get(id=device_id))

                fuel_types = []
                if request.POST.getlist('fuel_types'):
                    for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                        fuel_types.append(FuelType.objects.get(id=fuel_type_id))

                user = User.objects.get(id=request.user.id)
                get_car = CarModel.objects.get(id=request.POST.get('car'))

                # create car
                car = Car.objects.create(model=get_car)
                car.body_type = BodyType.objects.get(id=request.POST.get('body_type', None))
                if request.POST.get('chassis_number', None):
                    car.chassis_number = request.POST.get('chassis_number', None)

                if request.POST.get('lost_technical_passport') == 'true':
                    car.lost_technical_passport = True
                else:
                    car.old_technical_passport = request.POST.get('old_technical_passport', None)
                    car.lost_technical_passport = False

                if request.POST.get('lost_number') == 'true':
                    car.lost_number = True
                else:
                    car.old_number = request.POST.get('old_number', None)
                    car.lost_number = False

                if request.POST.get('is_old_number') == 'true':
                    car.is_old_number = True
                else:
                    car.is_old_number = False

                if request.POST.get('save_old_number') == 'true':
                    car.save_old_number = True
                    car.is_replace_number = False
                else:
                    car.save_old_number = False
                    car.is_replace_number = True

                if request.POST.get('is_auction') == 'true':
                    car.is_auction = True
                    car.given_number = request.POST.get('given_number', None)
                else:
                    car.is_auction = False
                car.body_number = body_number
                car.engine_number = engine_number
                car.type = CarType.objects.get(id=request.POST.get('car_type'))
                car.made_year = made_year
                car.full_weight = full_weight
                car.empty_weight = empty_weight
                car.engine_power = engine_power

                car.color = color
                for fuel_type in fuel_types:
                    car.fuel_type.add(fuel_type)
                for device in devices:
                    car.device.add(device)
                car.save()

                application = Application.objects.create(created_user=user, created_date=timezone.now())

                if int(person_type) == LEGAL_PERSON:
                    organization = Organization.objects.get(id=request.POST.get('organization'))
                    application.person_type = person_type
                    application.organization = organization
                password = random.randint(1000, 9999)
                application.password = password
                application.service = service
                application.car = car

                if request.POST.get('seriya', None) and request.POST.get('contract_date', None):
                    seriya = request.POST.get('seriya')
                    contract_date = datetime.datetime.strptime(request.POST.get('contract_date'), '%Y-%m-%d')
                    example_document = ExampleDocument.objects.get(key=service.key)
                    application_document = ApplicationDocument.objects.filter(application=application,
                                                                              example_document=example_document)
                    if not application_document.exists():
                        ApplicationDocument.objects.create(application=application,
                                                           example_document=example_document,
                                                           seriya=seriya,
                                                           contract_date=contract_date)

                application.save()
                return HttpResponse(application.id, content_type='json', status=200)
        except Exception as e:
            print(e)
            return HttpResponse(e, status=400)


class GiftAgreement(ServiceCustomMixin):
    template_name = 'service/gift_agreement/gift_agreement.html'

    def post(self, request, *args, **kwargs):
        return self.get_json_data()

    def get_json_data(self):
        try:
            with transaction.atomic():
                request = self.request
                service = Service.objects.get(key='gift_agreement')

                person_type = request.POST.get('person_type')
                engine_number = request.POST.get('engine_number')
                full_weight = request.POST.get('full_weight')
                empty_weight = request.POST.get('empty_weight')
                engine_power = request.POST.get('engine_power')
                body_number = request.POST.get('body_number')

                color = Color.objects.get(id=request.POST.get('color', None))
                made_year = datetime.datetime.strptime(request.POST.get('made_year', None), '%Y-%m-%d')

                devices = []
                if request.POST.getlist('devices'):
                    for device_id in list(filter(None, request.POST.getlist('devices'))):
                        devices.append(Device.objects.get(id=device_id))

                fuel_types = []
                if request.POST.getlist('fuel_types'):
                    for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                        fuel_types.append(FuelType.objects.get(id=fuel_type_id))

                user = User.objects.get(id=request.user.id)
                get_car = CarModel.objects.get(id=request.POST.get('car'))

                # create car
                car = Car.objects.create(model=get_car)
                car.body_type = BodyType.objects.get(id=request.POST.get('body_type', None))
                if request.POST.get('chassis_number', None):
                    car.chassis_number = request.POST.get('chassis_number', None)

                if request.POST.get('lost_technical_passport') == 'true':
                    car.lost_technical_passport = True
                else:
                    car.old_technical_passport = request.POST.get('old_technical_passport', None)
                    car.lost_technical_passport = False

                if request.POST.get('lost_number') == 'true':
                    car.lost_number = True
                else:
                    car.old_number = request.POST.get('old_number', None)
                    car.lost_number = False

                if request.POST.get('is_old_number') == 'true':
                    car.is_old_number = True
                else:
                    car.is_old_number = False

                if request.POST.get('is_auction') == 'true':
                    car.is_auction = True
                    car.given_number = request.POST.get('given_number', None)
                else:
                    car.is_auction = False
                car.body_number = body_number
                car.engine_number = engine_number
                car.type = CarType.objects.get(id=request.POST.get('car_type'))
                car.made_year = made_year
                car.full_weight = full_weight
                car.empty_weight = empty_weight
                car.engine_power = engine_power

                car.is_replace_number = True

                car.color = color
                for fuel_type in fuel_types:
                    car.fuel_type.add(fuel_type)
                for device in devices:
                    car.device.add(device)
                car.save()

                application = Application.objects.create(created_user=user, created_date=timezone.now())

                if int(person_type) == LEGAL_PERSON:
                    organization = Organization.objects.get(id=request.POST.get('organization'))
                    application.person_type = person_type
                    application.organization = organization
                password = random.randint(1000, 9999)
                application.password = password
                application.service = service
                application.car = car

                if request.POST.get('seriya', None) and request.POST.get('contract_date', None):
                    seriya = request.POST.get('seriya')
                    contract_date = datetime.datetime.strptime(request.POST.get('contract_date'), '%Y-%m-%d')
                    example_document = ExampleDocument.objects.get(key=service.key)
                    application_document = ApplicationDocument.objects.filter(application=application,
                                                                              example_document=example_document)
                    if not application_document.exists():
                        ApplicationDocument.objects.create(application=application,
                                                           example_document=example_document,
                                                           seriya=seriya,
                                                           contract_date=contract_date)
                application.save()
                return HttpResponse(application.id, content_type='json', status=200)
        except Exception as e:
            print(e)
            return HttpResponse(e, status=400)


class InheritanceAgreement(ServiceCustomMixin):
    template_name = 'service/inheritance_agreement/inheritance_agreement.html'

    def post(self, request, *args, **kwargs):
        return self.get_json_data()

    def get_json_data(self):
        try:
            request = self.request
            service = get_object_or_404(Service, key='inheritance_agreement')

            person_type = request.POST.get('person_type')
            engine_number = request.POST.get('engine_number')
            full_weight = request.POST.get('full_weight')
            empty_weight = request.POST.get('empty_weight')
            engine_power = request.POST.get('engine_power')
            body_number = request.POST.get('body_number')

            color = Color.objects.get(id=request.POST.get('color', None))
            made_year = datetime.datetime.strptime(request.POST.get('made_year', None), '%Y-%m-%d')

            devices = []
            if request.POST.getlist('devices'):
                for device_id in list(filter(None, request.POST.getlist('devices'))):
                    devices.append(Device.objects.get(id=device_id))

            fuel_types = []
            if request.POST.getlist('fuel_types'):
                for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                    fuel_types.append(FuelType.objects.get(id=fuel_type_id))

            user = User.objects.get(id=request.user.id)
            get_car = CarModel.objects.get(id=request.POST.get('car'))

            # create car
            car = Car.objects.create(model=get_car)
            car.body_type = BodyType.objects.get(id=request.POST.get('body_type', None))
            if request.POST.get('chassis_number', None):
                car.chassis_number = request.POST.get('chassis_number', None)

            if request.POST.get('lost_technical_passport') == 'true':
                car.lost_technical_passport = True
            else:
                car.old_technical_passport = request.POST.get('old_technical_passport', None)
                car.lost_technical_passport = False

            if request.POST.get('lost_number') == 'true':
                car.lost_number = True
            else:
                car.old_number = request.POST.get('old_number', None)
                car.lost_number = False

            if request.POST.get('is_old_number') == 'true':
                car.is_old_number = True
            else:
                car.is_old_number = False

            if request.POST.get('is_auction') == 'true':
                car.is_auction = True
                car.given_number = request.POST.get('given_number', None)
            else:
                car.is_auction = False
            car.body_number = body_number
            car.engine_number = engine_number
            car.type = CarType.objects.get(id=request.POST.get('car_type'))
            car.made_year = made_year
            car.full_weight = full_weight
            car.empty_weight = empty_weight
            car.engine_power = engine_power

            car.is_replace_number = True

            car.color = color
            for fuel_type in fuel_types:
                car.fuel_type.add(fuel_type)
            for device in devices:
                car.device.add(device)
            car.save()

            application = Application.objects.create(created_user=user, created_date=timezone.now())

            if int(person_type) == LEGAL_PERSON:
                organization = Organization.objects.get(id=request.POST.get('organization'))
                application.person_type = person_type
                application.organization = organization
            password = random.randint(1000, 9999)
            application.password = password
            application.service = service
            application.car = car

            if request.POST.get('seriya', None) and request.POST.get('contract_date', None):
                seriya = request.POST.get('seriya')
                contract_date = datetime.datetime.strptime(request.POST.get('contract_date'), '%Y-%m-%d')
                example_document = ExampleDocument.objects.get(key=service.key)
                application_document = ApplicationDocument.objects.filter(application=application,
                                                                          example_document=example_document)
                if not application_document.exists():
                    ApplicationDocument.objects.create(application=application,
                                                       example_document=example_document,
                                                       seriya=seriya,
                                                       contract_date=contract_date)
            application.save()
            return HttpResponse(application.id, content_type='json', status=200)
        except Exception as e:
            print(e)
            return HttpResponse(e, status=400)


class ReEquipment(ServiceCustomMixin):
    template_name = 'service/re_equipment/re_equipment.html'

    def post(self, request, *args, **kwargs):
        return self.get_json_data()

    def get_json_data(self):
        try:
            with transaction.atomic():
                request = self.request
                service = Service.objects.get(key='gift_agreement')

                person_type = request.POST.get('person_type')
                engine_number = request.POST.get('engine_number')
                full_weight = request.POST.get('full_weight')
                empty_weight = request.POST.get('empty_weight')
                engine_power = request.POST.get('engine_power')
                body_number = request.POST.get('body_number')

                color = Color.objects.get(id=request.POST.get('color', None))
                made_year = datetime.datetime.strptime(request.POST.get('made_year', None), '%Y-%m-%d')

                devices = []
                if request.POST.getlist('devices'):
                    for device_id in list(filter(None, request.POST.getlist('devices'))):
                        devices.append(Device.objects.get(id=device_id))

                fuel_types = []
                if request.POST.getlist('fuel_types'):
                    for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                        fuel_types.append(FuelType.objects.get(id=fuel_type_id))

                user = User.objects.get(id=request.user.id)
                get_car = CarModel.objects.get(id=request.POST.get('car'))

                # create car
                car = Car.objects.create(model=get_car)
                car.body_type = BodyType.objects.get(id=request.POST.get('body_type', None))
                if request.POST.get('chassis_number', None):
                    car.chassis_number = request.POST.get('chassis_number', None)

                if request.POST.get('lost_technical_passport') == 'true':
                    car.lost_technical_passport = True
                else:
                    car.old_technical_passport = request.POST.get('old_technical_passport', None)
                    car.lost_technical_passport = False

                if request.POST.get('lost_number') == 'true':
                    car.lost_number = True
                else:
                    car.old_number = request.POST.get('old_number', None)
                    car.lost_number = False

                if request.POST.get('is_old_number') == 'true':
                    car.is_old_number = True
                else:
                    car.is_old_number = False

                if request.POST.get('is_auction') == 'true':
                    car.is_auction = True
                    car.given_number = request.POST.get('given_number', None)
                else:
                    car.is_auction = False
                car.body_number = body_number
                car.engine_number = engine_number
                car.type = CarType.objects.get(id=request.POST.get('car_type'))
                car.made_year = made_year
                car.full_weight = full_weight
                car.empty_weight = empty_weight
                car.engine_power = engine_power

                car.is_replace_number = True

                car.color = color
                for fuel_type in fuel_types:
                    car.fuel_type.add(fuel_type)
                for device in devices:
                    car.device.add(device)
                car.save()

                application = Application.objects.create(created_user=user, created_date=timezone.now())

                if int(person_type) == LEGAL_PERSON:
                    organization = Organization.objects.get(id=request.POST.get('organization'))
                    application.person_type = person_type
                    application.organization = organization
                password = random.randint(1000, 9999)
                application.password = password
                application.service = service
                application.car = car

                # if request.POST.get('seriya', None) and request.POST.get('contract_date', None):
                #     seriya = request.POST.get('seriya')
                #     contract_date = datetime.datetime.strptime(request.POST.get('contract_date'), '%Y-%m-%d')
                #     example_document = ExampleDocument.objects.get(key=service.key)
                #     application_document = ApplicationDocument.objects.filter(application=application,
                #                                                               example_document=example_document)
                #     if not application_document.exists():
                #         ApplicationDocument.objects.create(application=application,
                #                                            example_document=example_document,
                #                                            seriya=seriya,
                #                                            contract_date=contract_date)
                application.save()
            return HttpResponse(application.id, content_type='json', status=200)
        except Exception as e:
            print(e)
            return HttpResponse(e, status=400)


class ReplaceTp(ServiceCustomMixin):
    template_name = 'service/replace_tp/replace_tp.html'

    def post(self, request, *args, **kwargs):
        return self.get_json_data()

    def get_json_data(self):
        print(self.request.POST)
        try:
            with transaction.atomic():
                request = self.request
                service = Service.objects.get(key='replace_tp')

                person_type = request.POST.get('person_type')
                engine_number = request.POST.get('engine_number')
                full_weight = request.POST.get('full_weight')
                empty_weight = request.POST.get('empty_weight')
                engine_power = request.POST.get('engine_power')
                body_number = request.POST.get('body_number')

                color = Color.objects.get(id=request.POST.get('color', None))
                made_year = datetime.datetime.strptime(request.POST.get('made_year', None), '%Y-%m-%d')

                devices = []
                if request.POST.getlist('devices'):
                    for device_id in list(filter(None, request.POST.getlist('devices'))):
                        devices.append(Device.objects.get(id=device_id))

                fuel_types = []
                if request.POST.getlist('fuel_types'):
                    for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                        fuel_types.append(FuelType.objects.get(id=fuel_type_id))

                user = User.objects.get(id=request.user.id)
                get_car = CarModel.objects.get(id=request.POST.get('car'))

                # create car
                car = Car.objects.create(model=get_car)

                car.body_type = BodyType.objects.get(id=request.POST.get('body_type', None))

                if request.POST.get('chassis_number', None):
                    car.chassis_number = request.POST.get('chassis_number', None)

                if request.POST.get('re_fuel_type', None):
                    car.re_fuel_type = FuelType.objects.get(id=request.POST.get('re_fuel_type', None))

                if request.POST.get('lost_technical_passport') == 'true':
                    car.lost_technical_passport = True
                else:
                    car.old_technical_passport = request.POST.get('old_technical_passport', None)
                    car.lost_technical_passport = False

                car.old_number = request.POST.get('old_number', None)

                car.body_number = body_number
                car.engine_number = engine_number
                car.type = CarType.objects.get(id=request.POST.get('car_type'))

                car.made_year = made_year
                car.full_weight = full_weight
                car.empty_weight = empty_weight
                car.engine_power = engine_power
                car.color = color
                for fuel_type in fuel_types:
                    car.fuel_type.add(fuel_type)
                for device in devices:
                    car.device.add(device)
                car.save()

                application = Application.objects.create(created_user=user, created_date=timezone.now())

                if int(person_type) == LEGAL_PERSON:
                    organization = Organization.objects.get(id=request.POST.get('organization'))
                    application.person_type = person_type
                    application.organization = organization
                password = random.randint(1000, 9999)
                application.password = password
                application.service = service
                application.car = car
                application.save()
                return HttpResponse(application.id, content_type='json', status=200)
        except Exception as e:
            print(e)
            return HttpResponse(e,status=400)


class ReplaceNumberAndTp(ServiceCustomMixin):
    template_name = 'service/replace_number_and_tp/replace_number_and_tp.html'

    def post(self, request, *args, **kwargs):
        return self.get_json_data()

    def get_json_data(self):
        print(self.request.POST)
        try:
            with transaction.atomic():
                request = self.request
                service = Service.objects.get(key='replace_number_and_tp')

                person_type = request.POST.get('person_type')
                engine_number = request.POST.get('engine_number')
                full_weight = request.POST.get('full_weight')
                empty_weight = request.POST.get('empty_weight')
                engine_power = request.POST.get('engine_power')
                body_number = request.POST.get('body_number')

                color = Color.objects.get(id=request.POST.get('color', None))
                made_year = datetime.datetime.strptime(request.POST.get('made_year', None), '%Y-%m-%d')

                devices = []
                if request.POST.getlist('devices'):
                    for device_id in list(filter(None, request.POST.getlist('devices'))):
                        devices.append(Device.objects.get(id=device_id))

                fuel_types = []
                if request.POST.getlist('fuel_types'):
                    for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                        fuel_types.append(FuelType.objects.get(id=fuel_type_id))

                user = User.objects.get(id=request.user.id)
                get_car = CarModel.objects.get(id=request.POST.get('car'))

                # create car
                car = Car.objects.create(model=get_car)
                car.body_type = BodyType.objects.get(id=request.POST.get('body_type', None))
                if request.POST.get('chassis_number', None):
                    car.chassis_number = request.POST.get('chassis_number', None)

                if request.POST.get('lost_technical_passport') == 'true':
                    car.lost_technical_passport = True
                else:
                    car.old_technical_passport = request.POST.get('old_technical_passport', None)
                    car.lost_technical_passport = False

                if request.POST.get('lost_number') == 'true':
                    car.lost_number = True
                else:
                    car.old_number = request.POST.get('old_number', None)
                    car.lost_number = False

                if request.POST.get('is_old_number') == 'true':
                    car.is_old_number = True
                else:
                    car.is_old_number = False

                if request.POST.get('is_auction') == 'true':
                    car.is_auction = True
                    car.given_number = request.POST.get('given_number', None)
                else:
                    car.is_auction = False
                car.body_number = body_number
                car.engine_number = engine_number
                car.type = CarType.objects.get(id=request.POST.get('car_type'))
                car.made_year = made_year
                car.full_weight = full_weight
                car.empty_weight = empty_weight
                car.engine_power = engine_power

                car.is_replace_number = True

                car.color = color
                for fuel_type in fuel_types:
                    car.fuel_type.add(fuel_type)
                for device in devices:
                    car.device.add(device)
                car.save()

                application = Application.objects.create(created_user=user, created_date=timezone.now())

                if int(person_type) == LEGAL_PERSON:
                    organization = Organization.objects.get(id=request.POST.get('organization'))
                    application.person_type = person_type
                    application.organization = organization
                password = random.randint(1000, 9999)
                application.password = password
                application.service = service
                application.car = car
                application.save()
                return HttpResponse(application.id, content_type='json', status=200)
        except Exception as e:
            print(e)
            return HttpResponse(status=400)


@login_required
def gift_agreement_index(request):


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
            made_year = datetime.datetime.strptime(request.POST.get('made_year', None), '%d.%m.%Y')
            devices = []
            if request.POST.getlist('devices'):
                for device_id in list(filter(None, request.POST.getlist('devices'))):
                    devices.append(get_object_or_404(Device, id=device_id))

            fuel_types = []
            if request.POST.getlist('fuel_types'):
                for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                    fuel_types.append(get_object_or_404(FuelType, id=fuel_type_id))

            seriya = request.POST.get('seriya')
            contract_date = datetime.datetime.strptime(request.POST.get('contract_date', None), '%d.%m.%Y')
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
            service = Service.objects.create(person_type=person_type, car=car, title='gift_agreement',
                                             contract_date=contract_date)
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
                'application': application.file_name
            }

            data = json.dumps(context)
            return HttpResponse(data, content_type='json')
        else:
            return HttpResponse(False)


@login_required
def contract_of_sale_index(request):


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
            made_year = datetime.datetime.strptime(request.POST.get('made_year', None), '%d.%m.%Y')
            devices = []
            if request.POST.getlist('devices'):
                for device_id in list(filter(None, request.POST.getlist('devices'))):
                    devices.append(get_object_or_404(Device, id=device_id))

            fuel_types = []
            if request.POST.getlist('fuel_types'):
                for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                    fuel_types.append(get_object_or_404(FuelType, id=fuel_type_id))

            seriya = request.POST.get('seriya')
            contract_date = datetime.datetime.strptime(request.POST.get('contract_date', None), '%d.%m.%Y')
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
            service = Service.objects.create(person_type=person_type, car=car, title='contract_of_sale',
                                             contract_date=contract_date)
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
            made_year = datetime.datetime.strptime(request.POST.get('made_year', None), '%d.%m.%Y')
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
                'application': application.file_name
            }

            data = json.dumps(context)
            return HttpResponse(data, content_type='json')
        else:
            return HttpResponse(False)


@login_required
def replace_number_and_tp_index(request):


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
            made_year = datetime.datetime.strptime(request.POST.get('made_year', None), '%d.%m.%Y')
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
                'application': application.file_name
            }

            data = json.dumps(context)
            return HttpResponse(data, content_type='json')
        else:
            return HttpResponse(False)


@login_required
def re_equipment_index(request):


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
            made_year = datetime.datetime.strptime(request.POST.get('made_year', None), '%d.%m.%Y')
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
        qs = super().get_queryset().filter(is_active=True).order_by('sort')
        return qs


class ServiceInfo(DetailView):
    model = Service
    template_name = 'services/service_info.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context.update(form_fields=ServiceInputField.objects.filter(service=self.kwargs.get('pk')))
        return context
