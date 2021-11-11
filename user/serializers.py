import random

from django.contrib.auth import get_user_model, authenticate, login
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from reception.api import SendSmsWithApi, SUCCESS
from reception.telegram_bot import send_message_to_developer
from user.models import (
    Region, Section
)

User = get_user_model()


class RegionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = [
            'id',
            'title',
            'sort',
            'is_active'
        ]


class DistrictDetailSerializer(serializers.ModelSerializer):
    region = RegionDetailSerializer()

    class Meta:
        model = Region
        fields = [
            'id',
            'region',
            'title',
            'sort',
            'is_active'
        ]


class QuarterDetailSerializer(serializers.ModelSerializer):
    district = DistrictDetailSerializer()

    class Meta:
        model = Region
        fields = [
            'id',
            'district',
            'title',
            'sort',
            'is_active'
        ]


class UserSerializer(serializers.ModelSerializer):
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
            'birthday',
            'region',
            'district',
            'quarter',
            'address',
        ]


class UserCreateSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'phone',
            'last_name',
            'first_name',
            'middle_name',
            'birthday',
            'region',
            'district',
            'quarter',
            'address',
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
        }

    def create(self, validated_data):
        password = str(random.randint(10000, 99999))
        validated_data['username'] = validated_data['phone']
        user = User(**validated_data)
        user.set_password(password)
        user.turbo = password
        user.save()

        user = authenticate(self.context['request'], username=user.username, password=user.turbo)
        if user is not None:
            login(self.context['request'], user)
        else:
            raise ValidationError({'error': 'User not found'})

        msg = f"E-RIB dasturidan ro'yhatdan o'tish uchun login va parolingiz: Login: {user.username} Parol: {user.turbo}"
        r = SendSmsWithApi(message=msg, phone=user.phone).get()

        if r != SUCCESS:
            send_message_to_developer(
                f'Sms jo\'natishda xatolik! Phone: {user.phone} Login: {user.username}\nParol: {user.turbo}')
        return user


class UserCreatePassportSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'phone',
            'last_name',
            'first_name',
            'middle_name',
            'birthday',
            'region',
            'district',
            'quarter',
            'address',
        ]

    def create(self, validated_data):
        password = str(random.randint(10000, 99999))
        validated_data['username'] = validated_data['phone']
        user = User(**validated_data)
        user.set_password(password)
        user.turbo = password
        user.save()
        return user


class SaveUserPassportSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'passport_seriya',
            'passport_number',
            'issue_by_whom',
        ]
        extra_kwargs = {
            'passport_seriya': {'required': True},
            'passport_number': {'required': True},
            'issue_by_whom': {'required': True},
        }

    def update(self, instance, validated_data):
        if not instance:
            raise ValidationError({'error': 'User not found'})
        for k, v in validated_data.items():
            setattr(instance, k, v)
            instance.save()

        return instance


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = ['id', 'parent', 'title', 'region', 'district', 'located_district', 'quarter', 'street', 'is_active', ]


class RegionSerializer(serializers.ModelSerializer):
    # sections = SectionSerializer(many=True, source='section_set')
    class Meta:
        model = Region
        fields = ['id', 'title', ]
