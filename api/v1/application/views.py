import re

from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1 import permissions
from api.v1.application import serializers
from api.v1.user.serializers import (CreateAccountStatementCarSerializer, CreateContractOfSaleCarSerializer,
                                     CreateGiftAgreementCarSerializer, CreateReplaceTpCarSerializer)
from application.models import (
    Application, LEGAL_PERSON
)
from service.models import (Service, ExampleDocument)


class CreateAccountStatement(APIView):
    example_doc = None
    service_key = 'account_statement'
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]

    def validate(self, attrs):
        errors = dict()

        if not attrs.get('applicant'):
            errors.update(applicant=['Arizachi topilmadi!'])

        if not attrs.get('person_type'):
            errors.update(person_type=['Arizachi shaxsi topilmadi!'])

        if not attrs.get('seriya'):
            errors.update(seriya=["Hisob ma'lumotnomasi seriyasi kiritilmagan!"])

        if not attrs.get('contract_date'):
            errors.update(contract_date=["Notarius shartnomasi tuzilgan sana kiritilmagan!"])

        example_doc = ExampleDocument.objects.filter(key=self.service_key)
        if not example_doc:
            errors.update(document=["ExampleDocument objects not found!"])

        if errors.__len__() > 0:
            raise ValidationError(errors)

        self.example_doc = example_doc.last()
        return attrs

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        service = Service.objects.get(key=self.service_key)
        applicant_id = data.get('applicant')

        self.validate(data)

        person_type = data.get('person_type')
        organization_id = data.get('organization', None)
        car_serializer = CreateAccountStatementCarSerializer(data=data)
        if car_serializer.is_valid():
            car_serializer.save()
            app_data = {'car': car_serializer.instance.id, 'service': service.id, 'applicant': applicant_id,
                        'person_type': person_type}
            if int(person_type) == LEGAL_PERSON:
                app_data['organization'] = organization_id
            app_serializer = serializers.CreateApplicationSerializer(data=app_data, context=self.request)
            if app_serializer.is_valid():
                app_serializer.save()
                doc_data = {'application': app_serializer.instance.id, 'example_document': self.example_doc.id,
                            'seriya': data['seriya'], 'contract_date': data['contract_date']}
                doc_serializer = serializers.CreateApplicationDocumentSerializer(data=doc_data)
                if doc_serializer.is_valid():
                    doc_serializer.save()
                    print(doc_serializer.instance)
                    return Response(app_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    print(doc_serializer.errors)
                    return Response(doc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                print(app_serializer.errors)
                return Response(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            print(car_serializer.errors)
            return Response(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateContractOfSale(APIView):
    example_doc = None
    service_key = 'contract_of_sale'
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]

    def validate(self, attrs):
        errors = dict()

        if not attrs.get('applicant'):
            errors.update(applicant=['Arizachi topilmadi!'])

        if not attrs.get('person_type'):
            errors.update(person_type=['Arizachi shaxsi topilmadi!'])

        if not attrs.get('seriya'):
            errors.update(seriya=["Hisob ma'lumotnomasi seriyasi kiritilmagan!"])

        if not attrs.get('contract_date'):
            errors.update(contract_date=["Notarius shartnomasi tuzilgan sana kiritilmagan!"])

        example_doc = ExampleDocument.objects.filter(key=self.service_key)
        if not example_doc:
            errors.update(document=["ExampleDocument objects not found!"])

        if errors.__len__() > 0:
            raise ValidationError(errors)

        self.example_doc = example_doc.last()
        return attrs

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        service = Service.objects.get(key=self.service_key)
        applicant_id = data.get('applicant')

        self.validate(data)

        person_type = data.get('person_type')
        organization_id = data.get('organization', None)
        car_serializer = CreateContractOfSaleCarSerializer(data=data)
        if car_serializer.is_valid():
            car_serializer.save()
            app_data = {'car': car_serializer.instance.id, 'service': service.id, 'applicant': applicant_id,
                        'person_type': person_type}
            if int(person_type) == LEGAL_PERSON:
                app_data['organization'] = organization_id
            app_serializer = serializers.CreateApplicationSerializer(data=app_data, context=self.request)
            if app_serializer.is_valid():
                app_serializer.save()
                doc_data = {'application': app_serializer.instance.id, 'example_document': self.example_doc.id,
                            'seriya': data['seriya'], 'contract_date': data['contract_date']}
                doc_serializer = serializers.CreateApplicationDocumentSerializer(data=doc_data)
                if doc_serializer.is_valid():
                    doc_serializer.save()
                    print(doc_serializer.instance)
                    return Response(app_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    print(doc_serializer.errors)
                    return Response(doc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                print(app_serializer.errors)
                return Response(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            print(car_serializer.errors)
            return Response(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateGiftAgreement(APIView):
    example_doc = None
    service_key = 'gift_agreement'
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]

    def validate(self, attrs):
        errors = dict()

        if not attrs.get('applicant'):
            errors.update(applicant=['Arizachi topilmadi!'])

        if not attrs.get('person_type'):
            errors.update(person_type=['Arizachi shaxsi topilmadi!'])

        if not attrs.get('seriya'):
            errors.update(seriya=["Hisob ma'lumotnomasi seriyasi kiritilmagan!"])

        if not attrs.get('contract_date'):
            errors.update(contract_date=["Notarius shartnomasi tuzilgan sana kiritilmagan!"])

        example_doc = ExampleDocument.objects.filter(key=self.service_key)
        if not example_doc:
            errors.update(document=["ExampleDocument objects not found!"])

        if errors.__len__() > 0:
            raise ValidationError(errors)

        self.example_doc = example_doc.last()
        return attrs

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        service = Service.objects.get(key=self.service_key)
        applicant_id = data.get('applicant')
        # data['model'] = int(''.join(filter(str.isdigit, data.pop('car'))))
        # data['contract_date'] = '2021-12-01'

        self.validate(data)

        person_type = data.get('person_type')
        organization_id = data.get('organization', None)
        car_serializer = CreateGiftAgreementCarSerializer(data=data)
        if car_serializer.is_valid():
            car_serializer.save()
            app_data = {'car': car_serializer.instance.id, 'service': service.id, 'applicant': applicant_id,
                        'person_type': person_type}
            if int(person_type) == LEGAL_PERSON:
                app_data['organization'] = organization_id
            app_serializer = serializers.CreateApplicationSerializer(data=app_data, context=self.request)
            if app_serializer.is_valid():
                app_serializer.save()
                doc_data = {'application': app_serializer.instance.id, 'example_document': self.example_doc.id,
                            'seriya': data['seriya'], 'contract_date': data['contract_date']}
                doc_serializer = serializers.CreateApplicationDocumentSerializer(data=doc_data)
                if doc_serializer.is_valid():
                    doc_serializer.save()
                    print(doc_serializer.instance)
                    return Response(app_serializer.data, status=status.HTTP_201_CREATED)
                else:
                    print(doc_serializer.errors)
                    return Response(doc_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

            else:
                print(app_serializer.errors)
                return Response(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            print(car_serializer.errors)
            return Response(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateReplaceTp(APIView):
    service_key = 'replace_tp'
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]

    def validate(self, attrs):
        errors = dict()

        if not attrs.get('applicant'):
            errors.update(applicant=['Arizachi topilmadi!'])

        if not attrs.get('person_type'):
            errors.update(person_type=['Arizachi shaxsi topilmadi!'])

        if errors.__len__() > 0:
            raise ValidationError(errors)
        return attrs

    def post(self, request, *args, **kwargs):
        data = request.data
        print(data)
        service = Service.objects.get(key=self.service_key)
        applicant_id = data.get('applicant')

        self.validate(data)

        person_type = data.get('person_type')
        organization_id = data.get('organization', None)
        car_serializer = CreateReplaceTpCarSerializer(data=data)
        if car_serializer.is_valid():
            car_serializer.save()
            app_data = {'car': car_serializer.instance.id, 'service': service.id, 'applicant': applicant_id,
                        'person_type': person_type}
            if int(person_type) == LEGAL_PERSON:
                app_data['organization'] = organization_id
            app_serializer = serializers.CreateApplicationSerializer(data=app_data, context=self.request)
            if app_serializer.is_valid():
                app_serializer.save()
                return Response(app_serializer.data, status=status.HTTP_201_CREATED)
            else:
                print(app_serializer.errors)
                return Response(app_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            print(car_serializer.errors)
            return Response(car_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SaveApplicationSection(generics.UpdateAPIView):
    queryset = Application.objects.filter(is_active=True)
    serializer_class = serializers.ApplicationDetailSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission
    ]
