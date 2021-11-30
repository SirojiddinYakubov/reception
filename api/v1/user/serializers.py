from rest_framework import serializers

from user.models import (
    User,
    Region,
    District,
    Quarter, Organization, Car, Color, CarModel, CarType, FuelType, BodyType, Section, Device
)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, write_only=True)


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
        model = District
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
        model = Quarter
        fields = [
            'id',
            'district',
            'title',
            'sort',
            'is_active'
        ]


class RegionSectionsListSerializer(serializers.ModelSerializer):
    region = RegionDetailSerializer()
    located_district = DistrictDetailSerializer()
    quarter = QuarterDetailSerializer()

    class Meta:
        model = Section
        fields = ['id', 'parent', 'title', 'region', 'district', 'located_district', 'quarter', 'street', 'is_active', ]

class UserDetailSerializer(serializers.ModelSerializer):
    region = RegionDetailSerializer()
    district = DistrictDetailSerializer()
    quarter = QuarterDetailSerializer()

    class Meta:
        model = User
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


class UserShortDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'phone',
            'last_name',
            'first_name',
            'middle_name',
        ]


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


class CarModelsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = [
            'id',
            'title',
            'creator',
            'is_local',
            'is_truck',
            'created_user',
            'created_date'
        ]

class CarColorsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = [
            'id',
            'title',
            'created_date',
            'created_user',
        ]

class CarTypesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarType
        fields = [
            'id',
            'title',
            'created_date',
        ]

class DevicesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Device
        fields = [
            'id',
            'title',
            'created_date',
        ]

class CarFuelTypesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelType
        fields = [
            'id',
            'title',
            'created_date',
        ]

class CarBodyTypesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BodyType
        fields = [
            'id',
            'title',
            'created_date',
        ]

class CreateCarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = [
            'id',
            'title',
            'creator',
            'is_local',
            'is_truck',
            'is_active',
            'created_user',
            'created_date',
        ]

    def create(self, validated_data):
        validated_data['created_user'] = self.context['request'].user
        validated_data['is_active'] = True
        return super().create(validated_data)


class CreateColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = [
            'id',
            'title',
            'is_active',
            'created_date',
            'created_user'
        ]

    def create(self, validated_data):
        validated_data['created_user'] = self.context['request'].user
        validated_data['is_active'] = True
        return super().create(validated_data)


class CreateCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'id',
            'model',
            'body_type',
            'fuel_type',
            'full_weight',
            'empty_weight',
            'type',
            'device',
            'body_number',
            'chassis_number',
            'engine_number',
            'made_year',
            'color',
            'engine_power',
            'price',
            'is_auction',
            'is_saved_number',
            'given_number',
        ]
        extra_kwargs = {
            'model': {'required': True},
            'body_type': {'required': True},
            'fuel_type': {'required': True},
            'full_weight': {'required': True},
            'empty_weight': {'required': True},
            'type': {'required': True},
            'body_number': {'required': True},
            'engine_number': {'required': True},
            'made_year': {'required': True},
            'color': {'required': True},
            'engine_power': {'required': True},
            'price': {'required': True},
            'is_auction': {'required': True},
            'is_saved_number': {'required': True},
        }

    def create(self, validated_data):
        validated_data['is_new'] = True
        validated_data['is_replace_number'] = True
        return super().create(validated_data)


class OrganizationDetailSerializer(serializers.ModelSerializer):
    applicant = UserShortDetailSerializer()
    created_user = UserShortDetailSerializer()

    class Meta:
        model = Organization
        fields = [
            'id',
            'title',
            'identification_number',
            'legal_address_region',
            'legal_address_district',
            'address_of_garage',
            'director',
            'created_user',
            'created_date',
            'updated_date',
            'is_active',
            'applicant',
        ]


class CarDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = [
            'id',
            'model',
            'body_type',
            'fuel_type',
            'full_weight',
            'empty_weight',
            'type',
            'device',
            'body_number',
            'chassis_number',
            'engine_number',
            'made_year',
            'color',
            'engine_power',
            'price',
            'is_auction',
            'given_number'
        ]


class CreateOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = [
            'id',
            'title',
            'identification_number',
            'legal_address_region',
            'legal_address_district',
            'address_of_garage',
            'director',
            'created_user',
            'created_date',
            'updated_date',
            'applicant',
        ]

        extra_kwargs = {
            'title': {'required': True},
            'identification_number': {'required': True},
            'legal_address_region': {'required': True},
            'legal_address_district': {'required': True},
            'address_of_garage': {'required': True},
            'director': {'required': True},
        }

    def create(self, validated_data):
        validated_data['created_user'] = self.context['request'].user
        return super().create(validated_data)
