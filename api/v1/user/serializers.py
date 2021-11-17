from rest_framework import serializers

from user.models import (
    User,
    Region,
    District,
    Quarter
)


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
