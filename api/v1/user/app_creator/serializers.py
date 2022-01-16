import random

from rest_framework import serializers

from api.v1.user.serializers import (
    RegionDetailSerializer,
    DistrictDetailSerializer, QuarterDetailSerializer
)
from reception.api import (SendSmsWithPlayMobile, SUCCESS, SendSmsWithApi)
from reception.telegram_bot import (send_message_to_developer)
from user.models import (
    Organization, User
)


class UserOrganizationsListSerializer(serializers.ModelSerializer):
    legal_address_region = RegionDetailSerializer()
    legal_address_district = DistrictDetailSerializer()

    class Meta:
        model = Organization
        fields = [
            'id',
            'title',
            'legal_address_region',
            'legal_address_district',
            'identification_number',
            'address_of_garage',
            'director',
            'created_user',
            'created_date',
            'updated_date',
            'is_active'
        ]

class SelfCreatedUsersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'last_name',
            'first_name',
            'middle_name',
        ]

class ApplicantListSerializer(serializers.ModelSerializer):
    region = RegionDetailSerializer()
    district = DistrictDetailSerializer()
    quarter = QuarterDetailSerializer()

    class Meta:
        model = User
        fields = [
            'id',
            'last_name',
            'first_name',
            'middle_name',
            'region',
            'district',
            'quarter'
        ]

class CreateApplicantSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()

    class Meta:
        model = User
        read_only_fields = ('id',)
        fields = [
            'id',
            'phone',
            'last_name',
            'first_name',
            'middle_name',
            'birthday',
            'region',
            'district',
            'quarter',
            'address',
            'passport_seriya',
            'passport_number',
            'issue_by_whom',
            'created_by'
        ]
        extra_kwargs = {
            'last_name': {'required': True},
            'first_name': {'required': True},
            'middle_name': {'required': True},
            'birthday': {'required': True},
            'region': {'required': True},
            'district': {'required': True},
            'quarter': {'required': True},
            'address': {'required': True},
            'passport_seriya': {'required': True},
            'passport_number': {'required': True},
            'issue_by_whom': {'required': True},
            'created_by': {'required': True},
        }

    def validate_phone(self, value):
        phone = int(''.join(filter(str.isdigit, value)))
        user = User.objects.filter(username=phone)
        if user:
            raise serializers.ValidationError("Tel raqam oldin ro'yhatdan o'tkazilgan!")
        return phone

    def create(self, validated_data):
        password = str(random.randint(10000, 99999))
        validated_data['username'] = validated_data['phone']
        user = User(**validated_data)
        user.set_password(password)
        user.turbo = password
        user.save()

        msg = f"E-RIB dasturidan ro'yhatdan o'tish uchun login va parolingiz: Login: {user.username} Parol: {user.turbo}. Qo\'shimcha ma\'lumot uchun tel:972800809"
        r = SendSmsWithPlayMobile(phone=user.phone, message=msg).get()
        print(msg)
        if not r == SUCCESS:
            r = SendSmsWithApi(message=msg, phone=user.phone).get()
        # r = 200
        if r != SUCCESS:
            send_message_to_developer(
                f'Sms jo\'natishda xatolik! Phone: {user.phone} Login: {user.username}\nParol: {user.turbo}')
        return user

    def to_representation(self, instance):
        context = super(CreateApplicantSerializer, self).to_representation(instance)
        context['region'] = RegionDetailSerializer(instance.region).data
        context['district'] = DistrictDetailSerializer(instance.district).data
        if instance.quarter:
            context['quarter'] = QuarterDetailSerializer(instance.quarter).data
        return context