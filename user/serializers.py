import random

from django.contrib.auth import get_user_model, authenticate, login
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from django.utils.translation import gettext as _
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


class UserUpdateSerializer(serializers.ModelSerializer):
    phone = serializers.CharField()
    password = serializers.CharField(write_only=True)

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
            'person_id',
            'password',
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
            'password': {'required': True},
            'person_id': {'required': True},

        }

    # def validate_password(self, password):
    #     if password:
    #         validate_password(password)
    #     return super().validate(password)

    def validate_phone(self, value):
        current_user_id = self.context['request'].user.id
        user = User.objects.exclude(id=current_user_id).filter(username=value)
        if user:
            raise serializers.ValidationError("Tel raqam oldin ro'yhatdan o'tkazilgan!")
        return value

    def update(self, instance, validated_data):
        instance.username = validated_data.get('phone')
        if password := validated_data.pop('password', None):
            instance.turbo = password
            instance.set_password(password)
        return super().update(instance, validated_data)


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


class RegionSerializer(serializers.ModelSerializer):
    # sections = SectionSerializer(many=True, source='section_set')
    class Meta:
        model = Region
        fields = ['id', 'title', ]


class SectionSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    located_district = DistrictDetailSerializer()
    quarter = QuarterDetailSerializer()

    class Meta:
        model = Section
        fields = ['id', 'parent', 'title', 'region', 'district', 'located_district', 'quarter', 'street', 'is_active', ]


class CreateUserAccountViewSerializer(serializers.ModelSerializer):
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

        msg = f"E-RIB dasturidan ro'yhatdan o'tish uchun login va parolingiz: Login: {user.username} Parol: {user.turbo}"
        r = SendSmsWithApi(message=msg, phone=user.phone).get()

        if r != SUCCESS:
            send_message_to_developer(
                f'Sms jo\'natishda xatolik! Phone: {user.phone} Login: {user.username}\nParol: {user.turbo}')
        return user
