import datetime
import json
import os
import random

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from docxtpl import DocxTemplate
from rest_framework.authtoken.models import Token

from account_statement.models import AccountStatement
from application.models import Application, Service
from contract_of_sale.models import ContractOfSale
from gift_agreement.models import GiftAgreement
from reception.settings import BASE_DIR
from user.models import *
from user.utils import render_to_pdf


@login_required
def applications_list(request):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))
    context = {}

    if request.user.role == '2':
        qs = Application.objects.filter(created_user__region=request.user.region)
        print(qs)
        if request.method == "GET":
            if request.GET.get('person_type'):
                qs = qs.filter(person_type=request.GET.get('person_type'))
                context.update(applications=qs)
            if request.GET.get('process'):
                qs = qs.filter(process=request.GET.get('process'))
                context.update(applications=qs)
        print(qs)
        context.update(applications=qs)
        return render(request, 'user/role/controller/controller_applications_list.html', context)
    elif request.user.role == '3':
        applications = Application.objects.filter(created_user__region=request.user.region)
        context.update(applications=applications)
        return render(request, 'user/role/checker/checker_applications_list.html', context)
    elif request.user.role == '4':
        applications = Application.objects.filter(created_user__region=request.user.region)
        context.update(applications=applications)
        return render(request, 'user/role/technical/technical_applications_list.html', context)
    else:
        applications = Application.objects.filter(created_user=request.user)
        context.update(applications=applications)



    return render(request, 'application/applications_list.html', context)


@login_required
def application_detail(request, id):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    application = get_object_or_404(Application, id=id)
    if application.created_user != request.user:
        return redirect(reverse_lazy('application:applications_list'))

    context = {
        'application': application
    }
    return render(request, 'application/application_detail.html', context)


@login_required
def application_pdf(request, id):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    application = get_object_or_404(Application, id=id)
    region = get_object_or_404(Region, id=application.created_user.region.id)

    context = {
        'now_date': datetime.datetime.strftime(timezone.now(), '%d.%m.%Y'),
        'created_date': datetime.datetime.strftime(application.created_date, '%d.%m.%Y'),
        'app': application,
        'region': region
    }
    template_name = 'application/application_detail_pdf.html'
    pdf = render_to_pdf(template_name, context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Ariza #%s.pdf" % (application.id)
        content = "attachment; filename=%s" % (filename)
        response['Content-Disposition'] = content
        return response


@login_required
def get_information(request):
    if request.is_ajax():
        user = get_object_or_404(User, id=request.GET.get('user'))
        application = get_object_or_404(Application, id=request.GET.get('application'))
        account_statement = get_object_or_404(AccountStatement, id=application.account_statement.id)

        context = {
            'user': f"{user.last_name} {user.first_name}",
            'account_statement_photo_url': account_statement.cert_photo.url
        }

        data = json.dumps(context)
        return HttpResponse(data, content_type='json')
    else:
        return False


@login_required
def create_application_doc(request, filename):
    application = get_object_or_404(Application, file_name=filename)
    service = get_object_or_404(Service, id=application.service.id)

    context = {}

    if service.account_statement is not None:
        service = Service.objects.filter(account_statement=service.account_statement.id).first()
        data = AccountStatement.objects.filter(id=service.account_statement.id).first()
        if data.organization is not None:
            organization = get_object_or_404(Organization, id=data.organization.id)
            print(organization)
            context.update(org=organization)
            doc = DocxTemplate(f"static{os.sep}online{os.sep}account_statement{os.sep}account_statement_legal.docx")

        else:
            doc = DocxTemplate(
                f"static{os.sep}online{os.sep}account_statement{os.sep}account_statement_person.docx")
    if service.gift_agreement is not None:
        service = Service.objects.filter(gift_agreement=service.gift_agreement.id).first()
        data = GiftAgreement.objects.filter(id=service.gift_agreement.id).first()
        if data.organization is not None:
            organization = get_object_or_404(Organization, id=data.organization.id)
            context.update(org=organization)
            doc = DocxTemplate(f"static{os.sep}online{os.sep}gift_agreement{os.sep}gift_agreement_legal.docx")

        else:
            doc = DocxTemplate(
                f"static{os.sep}online{os.sep}gift_agreement{os.sep}gift_agreement_person.docx")

    if service.contract_of_sale is not None:
        service = Service.objects.filter(contract_of_sale=service.contract_of_sale.id).first()
        data = ContractOfSale.objects.filter(id=service.contract_of_sale.id).first()
        if data.organization is not None:
            organization = get_object_or_404(Organization, id=data.organization.id)
            context.update(org=organization)
            doc = DocxTemplate(f"static{os.sep}online{os.sep}contract_of_sale{os.sep}contract_of_sale_legal.docx")

        else:
            doc = DocxTemplate(
                f"static{os.sep}online{os.sep}contract_of_sale{os.sep}contract_of_sale_person.docx")

    print('before')
    print(data.car)
    car = get_object_or_404(Car, id=data.car.id)

    devices_string = ', '.join([str(i).replace('"', "'") for i in car.devices.all()])

    context.update(data=data,
                   now_date=datetime.datetime.strftime(timezone.now(), '%d.%m.%Y'),
                   devices=devices_string,
                   car=car,
                   state=f"{data.seriya} {datetime.datetime.strftime(data.date_conclusion_contract, '%d.%m.%Y')}",
                   user=request.user,
                   birthday=datetime.datetime.strftime(request.user.birthday, '%d.%m.%Y'))

    car_model = get_object_or_404(CarModel, id=car.model.id)
    if car_model.is_truck:
        context.update(type='Yuk')
    else:
        context.update(type='Yengil')

    if car_model.is_local:
        context.update(local='Mahalliy')
    else:
        context.update(local="Chet el")

    if car.lost_technical_passport:
        context.update(lost_technical_passport=True)

    doc.render(context)
    response = HttpResponse(doc, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    filename = "Ariza #%s.docx" % (filename)
    content = "attachment; filename=%s" % (filename)
    response['Content-Disposition'] = content
    doc.save(response)
    return response

    # render context doc file
    # doc.render(context)
    # # save doc file in directory media/applications/
    # doc.save(f"media{os.sep}applications{os.sep}{application.file_name}.docx", )

    #
    # # file_bytes = io.BytesIO()
    # # doc.save(file_bytes)
    # # file_bytes.seek(0)
    # # application.file_doc.save('Lease #12345.doc', ContentFile(file_bytes.read()))
    # # application.save()
    #
    # pdf = convert('static/online/contract_of_sale/contract_of_sale_person.docx', "media/123.pdf")
    # print('after')
    # file = open('static/online/contract_of_sale/contract_of_sale_person.docx', 'rb')
    # data = file.read()
    # print('before')
    # print(data)
    # application.file_pdf = pdf
    # application.save()
    #
    # application.password = password
    # application.save()
    #
    #
    # doc = DocxTemplate(f"static{os.sep}online{os.sep}contract_of_sale{os.sep}123.docx")
    # context ={
    #     'now_date': datetime.datetime.strftime(timezone.now(), '%d.%m.%Y'),
    # }
    # doc.render(context)

@login_required
def view_application_service_data(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    try:
        context = {}
        if service.account_statement:
            account_statement = get_object_or_404(AccountStatement, id=service.account_statement.id)
            context.update(account_statement=account_statement)
            return render(request, 'account_statement/view_account_statement_data.html', context)
        elif service.gift_agreement:
            gift_agreement = get_object_or_404(GiftAgreement, id=service.gift_agreement.id)
            context.update(gift_agreement=gift_agreement)
            return render(request, 'gift_agreement/view_gift_agreement_data.html', context)
        elif service.contract_of_sale:
            contract_of_sale = get_object_or_404(ContractOfSale, id=service.contract_of_sale.id)
            context.update(contract_of_sale=contract_of_sale)
            return render(request, 'contract_of_sale/view_contract_of_sale_data.html', context)
        else:
            return HttpResponse('SERVICE NOT FOUND')

    except AttributeError:
        return HttpResponse('SERVICE NOT FOUND')
