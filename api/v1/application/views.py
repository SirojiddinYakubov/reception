import re

from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1 import permissions
from api.v1.application import serializers
from api.v1.application.serializers import CreateApplicationSerializer
from api.v1.user.serializers import (CreateCarSerializer)
from application.models import (
    Application, LEGAL_PERSON
)
from service.models import (Service)


class CreateAccountStatement(APIView):
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]

    def validate(self, attrs):
        if not attrs.get('applicant'):
            raise ValidationError('Arizachi topilmadi!')
        if not attrs.get('person_type'):
            raise ValidationError('Arizachi shaxsi topilmadi!')
        return attrs

    def post(self, request, *args, **kwargs):
        data = request.data
        self.validate(data)
        service = Service.objects.get(key='account_statement')
        data._mutable = True
        applicant_id = int(''.join(filter(str.isdigit, data.pop('applicant'))))
        data._mutable = False
        person_type = data.get('person_type')
        organization_id = data.get('organization', None)
        car_serializer = CreateCarSerializer(data=data)
        if car_serializer.is_valid():
            car_serializer.save()
            app_data = {'car': car_serializer.instance.id, 'service': service.id, 'applicant': applicant_id,
                        'person_type': person_type}
            if int(person_type) == LEGAL_PERSON:
                app_data['organization'] = organization_id
            print(app_data)
            app_serializer = CreateApplicationSerializer(data=app_data, context=self.request)
            if app_serializer.is_valid():
                app_serializer.save()
                print(app_serializer.data)
                return Response(app_serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(app_serializer.errors)
                return Response(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            print(car_serializer.errors)
            return Response(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
