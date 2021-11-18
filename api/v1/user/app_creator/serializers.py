from rest_framework import serializers

from api.v1.user.serializers import (
    RegionDetailSerializer,
    DistrictDetailSerializer
)
from user.models import (
    Organization
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
