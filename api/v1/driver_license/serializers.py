from rest_framework import serializers

from driver_license.models import (CallToExam)


class CallToExamSendSmsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallToExam
        fields = [
            'id',
            'pupil',
            'phone',
            'coming_date',
            'is_send'
        ]
