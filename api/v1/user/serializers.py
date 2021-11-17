from rest_framework import serializers

from user.models import User


class UserDetailSerializer(serializers.ModelSerializer):
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
