import datetime
import json

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from api.v1.application.utils import ApplicationSuccessCreatedMessage
from application.models import Application
from service.models import Service, ExampleDocument
from user.models import (User, BodyType, FuelType, CarType, Device, Color, Region, District, Section, Quarter)


class ApplicationTests(APITestCase):
    def setUp(self):
        self.username = '919791999'
        self.password = 'Sirojiddin'
        self.USER_CREATE_URL = '/api/v1/user/auth/users/'
        self.JWT_CREATE_URL = '/api/v1/user/auth/jwt/create/'
        self.CAR_MODEL_CREATE_URL = '/api/v1/user/create-car-model/'
        self.TOKEN_KEY = 'Bearer'
        self.created_user = None
        self.access = None
        self.refresh = None
        self.service = None
        self.car_model = None
        self.body_type = None
        self.fuel_type = None
        self.car_type = None
        self.device = None

    def test_contract_of_sale(self):
        # assert token_response.status_code == 200

        self.created_user = self.create_user()

        self.client.credentials(HTTP_AUTHORIZATION=self.TOKEN_KEY + ' ' + self.access)

        self.service = self.create_service()

        self.car_model = self.create_car_model()
        self.body_type = self.create_body_type()
        self.fuel_type = self.create_fuel_type()
        self.car_type = self.create_car_type()
        self.device = self.create_device()
        self.color = self.create_color()

        # print(self.created_user)
        # print(self.service)
        # print(self.car_model)
        # print(self.body_type)
        # print(self.fuel_type)
        # print(self.car_type)
        # print(self.device)
        # print(self.color)

        data = {'organization': 'undefined', 'applicant': self.created_user.id,
                'created_user': self.created_user.id, 'person_type': '0',
                'seriya': 'ASH546465465', 'contract_date': '2022-02-16', 'model': self.car_model.get('id'),
                'body_type': self.body_type.id,
                'type': self.car_type.id, 'fuel_type': [self.fuel_type.id], 'engine_number': 'XWD465465465465',
                'body_number': 'ZDX56445646545554', 'chassis_number': 'RAQAMSIZ', 'full_weight': '0',
                'empty_weight': '0', 'engine_power': '120', 'color': self.color.id,
                'lost_technical_passport': 'false',
                'old_technical_passport': 'AAF54564654', 'save_old_number': 'false', 'lost_number': 'false',
                'old_number': '80979HBA', 'is_old_number': 'false', 'is_saved_number': 'false',
                'given_number': '', 'is_auction': 'false', 'made_year': '2021-2-16', 'is_another_car': 'false'
                }

        response = self.client.post('/api/v1/application/create_contract_of_sale/', data, format='json', )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.send_application_to_section(response.data)

        application = Application.objects.first()
        ApplicationSuccessCreatedMessage(application).get()

    def create_user(self):
        data = {
            'username': self.username,
            'password': self.password,
        }
        response = self.client.post(self.USER_CREATE_URL, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = User.objects.get()

        self.assertEqual(user.username, self.username)

        user.phone = self.username
        user.save()

        token_response = self.client.post(self.JWT_CREATE_URL, data, format='json')

        self.assertEqual(token_response.status_code, status.HTTP_200_OK)

        self.assertEqual(list(token_response.data.keys()), ['refresh', 'access'])

        self.access = token_response.data.get('access')
        self.refresh = token_response.data.get('refresh')
        return User.objects.get()

    def create_car_model(self):
        data = {
            'title': 'Malibu',
            'creator': 'GM Uzbekistan',
            'is_local': True,
            'is_truck': False,
            'is_active': True,
            'created_user': self.created_user.id,
            'created_date': datetime.datetime.now()
        }

        response = self.client.post(self.CAR_MODEL_CREATE_URL, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        return response.data

    def create_body_type(self):
        return BodyType.objects.create(title='SEDAN')

    def create_fuel_type(self):
        return FuelType.objects.create(title='BENZIN')

    def create_car_type(self):
        return CarType.objects.create(title='UNIVERSAL')

    def create_device(self):
        return Device.objects.create(title="QO'SHIMCHA PEDAL")

    def create_color(self):
        return Color.objects.create(title="QORA")

    def create_service(self):
        service = Service.objects.create(
            short_title="Oldi sotdi shartnomasi",
            long_title="Oldi sotdi shartnomasi",
            key="contract_of_sale",
            desc="Agarda siz avval ro'yhatdan o'tkazilgan avtotransport vositasini "
                 " bozordan yoki TRADE-IN usulida sotib olgan bo'lsangiz, ushbu avtotransport "
                 "vositasini ushbu qismdan ro'yhatdan o'tkazishingiz mumkin",
            photo="https://www.pngkit.com/png/full/312-3127999_sell-your-junk-car-to-us-sale-car.png",
            deadline="1 kundan 3",
            instruction="Ariza jo'natish uchun Ariza topshirish formasiga kirib, ushbu formada so'ralgan "
                        "barcha ma'lumotlarni kiritish yoki YHXB RIB yoki TRIB'lar huzuridagi maxsus operatorlar"
                        " yordamidan foydalanishingiz mumkin.",
        )
        example_document = ExampleDocument.objects.create(key="contract_of_sale", title="Oldi sotdi shartnomasi")
        service.document.add(example_document)
        service.save()
        return service

    def create_section(self):
        region = Region.objects.create(title="Toshkent shahri")
        district = District.objects.create(region=region, title="Yunusobod tumani")
        quarter = Quarter.objects.create(district=district, title="Xiyobon MFY")
        section = Section.objects.create(title="Toshkent shahar IIB YHXB", region=region,
                                         located_district=district, quarter=quarter, street="Xiyobon ko'chasi",
                                         is_active=True, pay_for_service=True, pay_for_treasury=True)

        self.assertEqual(Section.objects.count(), 1)
        section.district.add(district)
        return section

    def send_application_to_section(self, application):

        section = self.create_section()

        data = {
            'section': section.id,
            'process': 0
        }

        response = self.client.patch(f"/api/v1/application/save/application/section/{application.get('id')}/", data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

