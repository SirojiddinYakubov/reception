import json
import random
import re

import pyotp
import requests
from django.contrib import auth
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1 import permissions
from api.v1.user import serializers
from application.models import Application
from application.templatetags.applications_tags import get_payment_score, get_state_duty_payment
from reception.api import PaymentByRequisites, SendSmsWithPlayMobile, SUCCESS, SendSmsWithApi, FAILED
from reception.settings import TOKEN_MAX_AGE
from reception.telegram_bot import send_message_to_developer
from service.models import GetPayFromCard, PaymentForTreasury, AmountBaseCalculation, KAPITALBANK
from user.models import (
    User,
    Organization, CarModel, Color, CarType, FuelType, BodyType, Sms, Region, District, Quarter, Section, Device
)
from user.utils import send_otp


class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = serializers.LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = auth.authenticate(username=serializer.validated_data['username'],
                                     password=serializer.validated_data['password'])
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
                    # if request.POST.get('remember_me') == 'on':
                    #     request.session.set_expiry(TOKEN_MAX_AGE)
                    print(user.is_authenticated)
                    serializer = serializers.UserShortDetailSerializer(user)
                    return Response(serializer.data, status=status.HTTP_200_OK)
                else:
                    return Response("Sizning profilingiz faol holatda emas!", status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response("Login yoki parol noto'g'ri!", status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = serializers.UserDetailSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission |
        permissions.AdministratorPermission |
        permissions.ModeratorPermission |
        permissions.RegionalControllerPermission |
        permissions.StateControllerPermission

    ]

    def get_object(self):
        user_id = self.kwargs.get('pk')
        user = self.get_queryset().filter(id=user_id).last()
        return user


class UserOrganizationsList(generics.ListAPIView):
    queryset = Organization.objects.filter(is_active=True)
    serializer_class = serializers.UserOrganizationsListSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]

    def get_queryset(self):
        qs = super().get_queryset().filter(applicant=self.request.user)
        return qs


class OrganizationsList(generics.ListAPIView):
    queryset = Organization.objects.filter(is_active=True)
    serializer_class = serializers.UserOrganizationsListSerializer
    permission_classes = [
        permissions.UserPermission
    ]

    def get_queryset(self):
        qs = super().get_queryset().filter(applicant=self.kwargs.get('pk'))
        return qs


class CarModelsList(generics.ListAPIView):
    queryset = CarModel.objects.filter(is_active=True)
    serializer_class = serializers.CarModelsListSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]


class CarColorsList(generics.ListAPIView):
    queryset = Color.objects.filter(is_active=True)
    serializer_class = serializers.CarColorsListSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]


class CarTypesList(generics.ListAPIView):
    queryset = CarType.objects.filter(is_active=True)
    serializer_class = serializers.CarTypesListSerializer
    permission_classes = [AllowAny]


class DevicesList(generics.ListAPIView):
    queryset = Device.objects.filter(is_active=True)
    serializer_class = serializers.DevicesListSerializer
    permission_classes = [AllowAny]


class RegionsList(generics.ListAPIView):
    queryset = Region.objects.filter(is_active=True)
    serializer_class = serializers.RegionDetailSerializer
    permission_classes = [AllowAny]


class SectionExistsRegionsList(generics.ListAPIView):
    queryset = Region.objects.filter(is_active=True, section__isnull=False, section__parent__isnull=False, section__is_active=True).distinct()
    serializer_class = serializers.RegionDetailSerializer
    permission_classes = [AllowAny]


class RegionDistrictsList(generics.ListAPIView):
    queryset = District.objects.filter(is_active=True)
    serializer_class = serializers.DistrictDetailSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return self.queryset.filter(region_id=self.kwargs.get('pk'))


class RegionSectionsList(generics.ListAPIView):
    queryset = Section.objects.filter(is_active=True, parent__isnull=False)
    serializer_class = serializers.RegionSectionsListSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission |
        permissions.RegionalControllerPermission |
        permissions.ModeratorPermission |
        permissions.StateControllerPermission
    ]

    def get_queryset(self):
        return self.queryset.filter(region_id=self.kwargs.get('pk')).distinct()


class DistrictQuartersList(generics.ListAPIView):
    queryset = Quarter.objects.filter(is_active=True)
    serializer_class = serializers.QuarterDetailSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission |
        permissions.AdministratorPermission
    ]

    def get_queryset(self):
        return self.queryset.filter(district_id=self.kwargs.get('pk'))


class CarFuelTypesList(generics.ListAPIView):
    queryset = FuelType.objects.filter(is_active=True)
    serializer_class = serializers.CarFuelTypesListSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]


class CarBodyTypesList(generics.ListAPIView):
    queryset = BodyType.objects.filter(is_active=True)
    serializer_class = serializers.CarBodyTypesListSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]


class CreateOrganization(generics.CreateAPIView):
    queryset = Organization.objects.all()
    serializer_class = serializers.CreateOrganizationSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]

class CreateCarModel(generics.CreateAPIView):
    queryset = CarModel.objects.filter(is_active=True)
    serializer_class = serializers.CreateCarModelSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]

    def post(self, request, *args, **kwargs):
        if request.data.get('title'):
            model = CarModel.objects.filter(title__icontains=request.data.get('title').lower())
            if model.exists():
                return Response(status=status.HTTP_409_CONFLICT)
        return super().post(request, *args, **kwargs)


class CreateColor(generics.CreateAPIView):
    queryset = Color.objects.filter(is_active=True)
    serializer_class = serializers.CreateColorSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]

    def post(self, request, *args, **kwargs):
        if request.data.get('title'):
            color = Color.objects.filter(title__icontains=request.data.get('title').lower())
            if color.exists():
                return Response(status=status.HTTP_409_CONFLICT)
        return super().post(request, *args, **kwargs)


class GetCode(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone')
        phone = re.sub('[^0-9]', '', phone_number)
        user = User.objects.filter(username=phone)
        if user:
            return Response({'error': 'Phone Number already exists'},
                            status=status.HTTP_409_CONFLICT)

        otp_response = send_otp(phone_number)
        print(otp_response)
        send_message_to_developer(str(otp_response))
        msg = f"E-RIB dasturidan ro'yhatdan o'tish uchun tasdiqlash kodi: {otp_response['otp']}. Qo\'shimcha ma\'lumot uchun tel:972800809"
        r = SendSmsWithPlayMobile(phone=phone, message=msg).get()
        if not r == SUCCESS:
            r = SendSmsWithApi(message=msg, phone=phone).get()
        if r == SUCCESS:
            return Response({'secret': otp_response['secret']}, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Sms service not working"}, status=status.HTTP_400_BAD_REQUEST)

class VerifyCode(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        secret = request.data.get('secret')
        sms_code: str = request.data.get("code")
        sms_code = sms_code.zfill(6)
        if sms_code and secret:
            totp = pyotp.TOTP(secret, interval=315360000)
            if totp.verify(sms_code):
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Tasdiqlash kodi noto\'g\'ri!'}, status=status.HTTP_400_BAD_REQUEST)


class PlayMobileSmsStatus(APIView):
    def post(self, request, *args, **kwargs):
        """пример запроса статуса:
        { “messages”: {
            “message-id”: “exb48879”,
            “channel”: “SMS”,
            “status”: “Delivered”,
            “status-date”: “2019-11-23 12:23:10”,
            “description”: “”
            }
        }
        """
        # sms = Sms.objects.filter(sms_id=)
        send_message_to_developer(str(request.POST))
        return Response({'status': 'OK'}, status=status.HTTP_200_OK)


class GetCardPhoneNumber(APIView):
    permission_classes = [
        AllowAny
    ]

    def post(self, request, *args, **kwargs):
        self.card_number = request.data.get('card_number')
        self.exp_date = f"{request.data.get('exp_date')[2:4]}{request.data.get('exp_date')[0:2]}"

        response = PaymentByRequisites().get_card_phone_number(self.card_number, self.exp_date)
        if response['status'] == SUCCESS:
            phone = response['result']
            otp_response = send_otp(phone)
            send_message_to_developer(str(otp_response))
            msg = f"Ushbu kodni begona shaxslarga taqdim etmang!: {otp_response['otp']}"
            print(msg)
            r = SendSmsWithPlayMobile(phone=phone, message=msg).get()
            if not r == SUCCESS:
                r = SendSmsWithApi(message=msg, phone=phone).get()
            # r = 200
            if r == SUCCESS:
                return Response({'secret': otp_response['secret'], 'phone': phone}, status=status.HTTP_200_OK)
            else:
                return Response("Profilaktika ishlari olib borilmoqda! Iltimos keyinroq urinib ko'ring!",
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(response['result'], status=status.HTTP_400_BAD_REQUEST)


class ConfirmPay(APIView):
    permission_classes = [AllowAny]

    card_number = None
    exp_date = None
    application_id = None
    percent_id = None
    score = None

    def post(self, request, *args, **kwargs):
        self.card_number = request.data.get('card_number')
        self.exp_date = f"{request.data.get('exp_date')[2:4]}{request.data.get('exp_date')[0:2]}"
        self.percent_id = request.data.get('percent')
        self.application_id = request.data.get('application')
        self.score = get_payment_score(self.application_id, self.percent_id)
        amount_base_calculation = AmountBaseCalculation.objects.filter(is_active=True).order_by('-id').last()
        application = Application.objects.get(id=self.application_id)

        amount = get_state_duty_payment(self.percent_id, self.application_id)
        if not amount == FAILED:
            commission_amount = amount / 100 * 2
            all_amount = amount + commission_amount
            transaction = PaymentByRequisites().get_pay_from_card(self.card_number, self.exp_date, all_amount * 100)
            if transaction['status'] == SUCCESS:
                GetPayFromCard.objects.create(application_id=self.application_id, amount=all_amount,
                                              transaction_id=transaction['result'])
                payment = PaymentForTreasury.objects.create(application_id=self.application_id,
                                                            amount=amount, state_duty_score=self.score,
                                                            state_duty_percent_id=self.percent_id,
                                                            amount_base_calculation=amount_base_calculation,
                                                            payment_system=KAPITALBANK,
                                                            status=PaymentForTreasury.PROCESSING)

                text = f'{self.application_id}-raqamli arizangizga muvofiq, {amount} so\'m bankka muvafaqiyatli jo\'natildi. Bank tomonidan to\'lov qabul qilinganidan so\'ng sms xabarnoma olasiz. Ushbu jarayon bir necha soatgacha cho\'zilishi mumkin. Banklar ishlamaydigan kunlari o\'tkazilgan to\'lovlar, keyingi bank ish kuniga qadar cho\'zilishi mumkin. Qo\'shimcha ma\'lumot uchun tel:972800809'

                if application.applicant:
                    phone = application.applicant.phone
                else:
                    phone = application.created_user.phone
                r = SendSmsWithPlayMobile(phone=phone, message=text).get()
                SendSmsWithPlayMobile(phone=972800809,
                                      message=f"{application.id}-raqamli arizaga asosan, {phone} dan {all_amount} so'm to'landi!").get()
                SendSmsWithPlayMobile(phone=919791999,
                                      message=f"{application.id}-raqamli arizaga asosan, {phone} dan {all_amount} so'm to'landi!").get()
                print(text)
                if not r == SUCCESS:
                    # send sms with eskiz
                    r = SendSmsWithApi(message=text, phone=phone).get()

                if r != SUCCESS:
                    send_message_to_developer(f'Sms services not working!')

                print(transaction)
                return Response('OK', status=status.HTTP_200_OK)
            else:
                print(transaction)
                return Response(transaction['result'], status=status.HTTP_400_BAD_REQUEST)
        else:
            send_message_to_developer(
                f'get_state_duty_payment function not working! Variables: percent_id: {self.percent_id}, application_id: {self.application_id}')
            return Response("Xatolik! Iltimos keyinroq urinib ko'ring!", status=status.HTTP_400_BAD_REQUEST)
