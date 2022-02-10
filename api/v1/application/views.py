import datetime
import os
import re

from django.http import HttpResponse
from django.utils import timezone
from docxtpl import DocxTemplate
from reportlab.pdfgen import canvas
from rest_framework import generics, status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1 import permissions
from api.v1.application import serializers
from api.v1.service.serializers import StateDutyPercentDetailSerializer, StateDutyScoreDetailSerializer
from api.v1.user.serializers import (CreateAccountStatementCarSerializer, CreateContractOfSaleCarSerializer,
                                     CreateGiftAgreementCarSerializer, CreateReplaceTpCarSerializer,
                                     CreateInheritanceAgreementCarSerializer, CreateReplaceNumberAndTpCarSerializer)
from application.models import (
    Application, LEGAL_PERSON, DRAFT, ApplicationDocument, SHIPPED, DocumentForPolice
)
from application.serializers import DocumentForPoliceSerializer
from application.templatetags.applications_tags import get_payment_score
from application.utils import filter_state_duty_percents
from reception.api import SendSmsWithPlayMobile, SUCCESS, SendSmsWithApi
from reception.telegram_bot import send_message_to_developer
from service.models import (Service, ExampleDocument, AmountBaseCalculation, StateDutyPercent)
from user.models import Section, Car, CarModel, CHECKER, User
from user.utils import render_to_pdf


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
            errors.update(seriya=["Oldi sotdi shartnomasi seriyasi kiritilmagan!"])

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


class CreateAuctionProtocol(APIView):
    example_doc = None
    service_key = 'auction_protocol'
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
            errors.update(seriya=["Auksion bayonnomasi seriyasi kiritilmagan!"])

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


class CreateCreditContract(APIView):
    example_doc = None
    service_key = 'credit_contract'
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
            errors.update(seriya=["Kredit shartnomasi seriyasi va raqami kiritilmagan!"])

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
            errors.update(seriya=["Xadya shartnomasi seriyasi kiritilmagan!"])

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


class CreateInheritanceAgreement(APIView):
    example_doc = None
    service_key = 'inheritance_agreement'
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
            errors.update(seriya=["Me'ros shartnomasi seriyasi kiritilmagan!"])

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
        car_serializer = CreateInheritanceAgreementCarSerializer(data=data)
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


class CreateReplaceNumberAndTp(APIView):
    service_key = 'replace_number_and_tp'
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
        car_serializer = CreateReplaceNumberAndTpCarSerializer(data=data)
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
    serializer_class = serializers.ApplicationSectionUpdateSerializer
    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission |
        permissions.ModeratorPermission |
        permissions.AdministratorPermission |
        permissions.RegionalControllerPermission |
        permissions.CheckerPermission
    ]


class GenerateApplicationWord(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        filename = kwargs.get('filename')
        application = Application.objects.get(file_name=filename)

        if application.process == DRAFT:
            return Response("Ariza nusxasini yuklab olish uchun arizani to'liq to'ldiring!",
                            status=status.HTTP_400_BAD_REQUEST)

        section = Section.objects.get(id=application.section.id)

        if application.is_block:
            return Response("Ariza nusxasini yuklab olish uchun arizani faollashtirishingiz talab etiladi!",
                            status=status.HTTP_400_BAD_REQUEST)

        service = Service.objects.get(id=application.service.id)

        context = {}
        if application.organization:
            doc = DocxTemplate(f"static{os.sep}online{os.sep}{service.key}{os.sep}{service.key}_legal.docx")
        else:
            doc = DocxTemplate(f"static{os.sep}online{os.sep}{service.key}{os.sep}{service.key}_person.docx")

        car = Car.objects.get(id=application.car.id)

        devices_string = ', '.join([str(i).replace('"', "'") for i in car.device.all()])
        fuel_types_string = ', '.join([str(i).replace('"', "'") for i in car.fuel_type.all()])
        re_fuel_type_string = car.re_fuel_type.title if car.re_fuel_type else ''

        application_document = ApplicationDocument.objects.filter(example_document__key=service.key,
                                                                  application=application).last()

        if application_document and application_document.contract_date:
            context.update(
                state=f"{application_document.seriya} {application_document.contract_date.strftime('%d.%m.%Y')}")

        if car.given_technical_passport:
            context.update(given_technical_passport=car.given_technical_passport)
        if application.organization:
            context.update(org=application.organization)
            context.update(
                legal_address=f"{application.organization.legal_address_region.title}, {application.organization.legal_address_district.title}")
        context.update(now_date=datetime.datetime.strftime(timezone.now(), '%d.%m.%Y'),
                       devices=devices_string,
                       fuel_types=fuel_types_string,
                       car=car,
                       made_year=car.made_year.strftime("%d.%m.%Y"),
                       user=application.applicant if application.applicant else application.created_user,
                       birthday=application.applicant.birthday.strftime(
                           '%d.%m.%Y') if application.applicant else application.created_user.birthday.strftime(
                           '%d.%m.%Y'),
                       given_number=car.given_number,
                       old_number=car.old_number,
                       old_technical_passport=car.old_technical_passport,
                       re_fuel_type=re_fuel_type_string,
                       section=section)

        car_model = CarModel.objects.get(id=car.model.id)

        if car_model.is_local:
            context.update(local='Mahalliy')
        else:
            context.update(local="Chet el")

        if car.lost_technical_passport:
            context.update(lost_technical_passport=True)

        doc.render(context)
        response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
        filename = "Ariza #%s.docx" % (filename)
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        doc.save(response)
        return response


class GenerateApplicationPdf(generics.ListAPIView):
    def get(self, request, *args, **kwargs):
        application = Application.objects.get(id=kwargs.get('pk'))
        pdf = render_to_pdf('application/application_detail_pdf.html', self.get_context_data())
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Ariza #%s.pdf" % (application.id)
            content = "attachment; filename=%s" % (filename)
            response['Content-Disposition'] = content
            return response

    def get_context_data(self, *args, **kwargs):
        application = Application.objects.get(id=self.kwargs.get('pk'))
        context = {
            'now_date': timezone.now(),
            'created_date': application.created_date,
            'app': application,
            'section': application.section,
            'request': self.request,
        }
        return context


class SendApplicationToSection(generics.ListAPIView):
    def post(self, request, *args, **kwargs):
        try:
            application_id = kwargs.get('pk')
            application = Application.objects.get(id=application_id)
            base_amount = AmountBaseCalculation.objects.filter(is_active=True).last()
            if not base_amount:
                return Response("Eng kam oylik ish haqi topilmadi!", status=status.HTTP_400_BAD_REQUEST)

            if application.process == DRAFT:
                return Response("Ariza to'liq to'ldirilmagan!", status=status.HTTP_400_BAD_REQUEST)

            if application.is_block:
                return Response(
                    f"Ariza aktivlashtirilmagan! Arizani {application.section.title} ga jo'natish uchun {int(base_amount.amount / 100 * 5)} so'm to'lov qilishingiz kerak",
                    status=status.HTTP_400_BAD_REQUEST)
            application.process = SHIPPED
            application.save()

            text = f"E-RIB.UZ Onlayn ariza platformasiga {application.id}-raqamli ariza kelib tushdi. \nIltimos arizani ko'rib chiqish uchun qabul qiling. Fuqaro sizning javobingizni kutmoqda!"
            inspectors = User.objects.filter(section=application.section, role=CHECKER)

            if inspectors:
                for inspector in inspectors:
                    r = SendSmsWithPlayMobile(phone=inspector.phone, message=text).get()
                    if not r == SUCCESS:
                        r = SendSmsWithApi(message=text, phone=inspector.phone).get()
                        if not r == SUCCESS:
                            send_message_to_developer('Sms service not working!')

            document_polices = DocumentForPolice.objects.filter(is_active=True, service=application.service)
            serializer = DocumentForPoliceSerializer(document_polices, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response("Xatolik yuz berdi!", status=status.HTTP_400_BAD_REQUEST)


class GetPaymentPercents(APIView):
    def get(self, request, *args, **kwargs):
        application = Application.objects.get(id=kwargs.get('pk'))
        percents = filter_state_duty_percents(application)
        serializer = serializers.ApplicationPaymentStateDutyPercentSerializer(percents, many=True,
                                                                              context={'application': application})
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetPaymentScore(APIView):
    def get(self, request, *args, **kwargs):
        score = get_payment_score(kwargs.get('application_id'), kwargs.get('percent_id'))
        serializer = StateDutyScoreDetailSerializer(score)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ApplicationDetail(generics.RetrieveAPIView):
    queryset = Application.objects.filter(is_active=True)
    serializer_class = serializers.ApplicationDetailFullSerializer

    permission_classes = [
        permissions.UserPermission |
        permissions.AppCreatorPermission |
        permissions.AdministratorPermission |
        permissions.ModeratorPermission |
        permissions.RegionalControllerPermission |
        permissions.CheckerPermission
    ]

    def get_object(self):
        application = self.get_queryset().filter(id=self.kwargs.get('pk')).last()
        return application
