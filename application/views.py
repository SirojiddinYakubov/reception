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


from application.models import *
from reception.settings import BASE_DIR
from service.utils import calculation_state_duty_service_price
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
        if request.method == "GET":
            if request.GET.get('service'):
                if request.GET.get('service') == 'account_statement':
                    qs = qs.filter(service__title='account_statement')
                    context.update(applications=qs)
                if request.GET.get('service') == 'gift_agreement':
                    qs = qs.filter(service__title='gift_agreement')
                    context.update(applications=qs)
                if request.GET.get('service') == 'contract_of_sale':
                    qs = qs.filter(service__title='contract_of_sale')
                    context.update(applications=qs)
            if request.GET.get('person_type'):
                qs = qs.filter(person_type=request.GET.get('person_type'))
                context.update(applications=qs)
            if request.GET.get('process'):
                qs = qs.filter(process=request.GET.get('process'))
                context.update(applications=qs)
            if request.GET.get('payment'):
                qs = qs.filter(is_payment=request.GET.get('payment'))
                context.update(applications=qs)
            if request.GET.get('technical'):
                qs = qs.filter(service__car__is_confirm=request.GET.get('technical'))
                context.update(applications=qs)
            if request.GET.get('date'):
                today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
                today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
                some_day_last_week = datetime.datetime.combine(timezone.now().date() - datetime.timedelta(days=7),datetime.time.min)
                some_day_last_month = datetime.datetime.combine(today_min.replace(day=1),datetime.time.min)
                some_day_last_year = datetime.datetime.combine(today_min.replace(month=1, day=1), datetime.time.min)

                if request.GET.get('date') == 'today':
                    qs = qs.filter(created_date__range=(today_min, today_max))
                    context.update(applications=qs)
                if request.GET.get('date') == 'last-7-days':
                    qs = qs.filter(created_date__range=(some_day_last_week, today_max))
                    context.update(applications=qs)
                if request.GET.get('date') == 'month':
                    qs = qs.filter(created_date__range=(some_day_last_month, today_max))
                    context.update(applications=qs)
                if request.GET.get('date') == 'year':
                    qs = qs.filter(created_date__range=(some_day_last_year, today_max))
                    context.update(applications=qs)
        context.update(applications=qs)
        return render(request, 'user/role/controller/controller_applications_list.html', context)
    elif request.user.role == '3':
        qs = Application.objects.filter(created_user__region=request.user.region)
        if request.method == "GET":
            if request.GET.get('service'):
                if request.GET.get('service') == 'account_statement':
                    qs = qs.filter(service__title='account_statement')
                    context.update(applications=qs)
                if request.GET.get('service') == 'gift_agreement':
                    qs = qs.filter(service__title='gift_agreement')
                    context.update(applications=qs)
                if request.GET.get('service') == 'contract_of_sale':
                    qs = qs.filter(service__title='contract_of_sale')
                    context.update(applications=qs)
            if request.GET.get('person_type'):
                qs = qs.filter(person_type=request.GET.get('person_type'))
                context.update(applications=qs)
            if request.GET.get('process'):
                qs = qs.filter(process=request.GET.get('process'))
                context.update(applications=qs)
            if request.GET.get('payment'):
                qs = qs.filter(is_payment=request.GET.get('payment'))
                context.update(applications=qs)
            if request.GET.get('technical'):
                qs = qs.filter(service__car__is_confirm=request.GET.get('technical'))
                context.update(applications=qs)
            if request.GET.get('date'):
                today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
                today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
                some_day_last_week = datetime.datetime.combine(timezone.now().date() - datetime.timedelta(days=7),datetime.time.min)
                some_day_last_month = datetime.datetime.combine(today_min.replace(day=1),datetime.time.min)
                some_day_last_year = datetime.datetime.combine(today_min.replace(month=1, day=1), datetime.time.min)

                if request.GET.get('date') == 'today':
                    qs = qs.filter(created_date__range=(today_min, today_max))
                    context.update(applications=qs)
                if request.GET.get('date') == 'last-7-days':
                    qs = qs.filter(created_date__range=(some_day_last_week, today_max))
                    context.update(applications=qs)
                if request.GET.get('date') == 'month':
                    qs = qs.filter(created_date__range=(some_day_last_month, today_max))
                    context.update(applications=qs)
                if request.GET.get('date') == 'year':
                    qs = qs.filter(created_date__range=(some_day_last_year, today_max))
                    context.update(applications=qs)
        context.update(applications=qs)
        return render(request, 'user/role/checker/checker_applications_list.html', context)
    elif request.user.role == '4':
        qs = Application.objects.filter(created_user__region=request.user.region)
        if request.method == "GET":
            if request.GET.get('service'):
                if request.GET.get('service') == 'account_statement':
                    qs = qs.filter(service__title='account_statement')
                    context.update(applications=qs)
                if request.GET.get('service') == 'gift_agreement':
                    qs = qs.filter(service__title='gift_agreement')
                    context.update(applications=qs)
                if request.GET.get('service') == 'contract_of_sale':
                    qs = qs.filter(service__title='contract_of_sale')
                    context.update(applications=qs)
            if request.GET.get('person_type'):
                qs = qs.filter(person_type=request.GET.get('person_type'))
                context.update(applications=qs)
            if request.GET.get('process'):
                qs = qs.filter(process=request.GET.get('process'))
                context.update(applications=qs)
            if request.GET.get('payment'):
                qs = qs.filter(is_payment=request.GET.get('payment'))
                context.update(applications=qs)
            if request.GET.get('technical'):
                qs = qs.filter(service__car__is_confirm=request.GET.get('technical'))
                context.update(applications=qs)
            if request.GET.get('date'):
                today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
                today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
                some_day_last_week = datetime.datetime.combine(timezone.now().date() - datetime.timedelta(days=7),datetime.time.min)
                some_day_last_month = datetime.datetime.combine(today_min.replace(day=1),datetime.time.min)
                some_day_last_year = datetime.datetime.combine(today_min.replace(month=1, day=1), datetime.time.min)

                if request.GET.get('date') == 'today':
                    qs = qs.filter(created_date__range=(today_min, today_max))
                    context.update(applications=qs)
                if request.GET.get('date') == 'last-7-days':
                    qs = qs.filter(created_date__range=(some_day_last_week, today_max))
                    context.update(applications=qs)
                if request.GET.get('date') == 'month':
                    qs = qs.filter(created_date__range=(some_day_last_month, today_max))
                    context.update(applications=qs)
                if request.GET.get('date') == 'year':
                    qs = qs.filter(created_date__range=(some_day_last_year, today_max))
                    context.update(applications=qs)
        context.update(applications=qs)
        return render(request, 'user/role/technical/technical_applications_list.html', context)
    else:
        qs = Application.objects.filter(created_user=request.user)
        if request.method == "GET":
            if request.GET.get('service'):
                if request.GET.get('service') == 'account_statement':
                    qs = qs.filter(service__title='account_statement')
                    context.update(applications=qs)
                if request.GET.get('service') == 'gift_agreement':
                    qs = qs.filter(service__title='gift_agreement')
                    context.update(applications=qs)
                if request.GET.get('service') == 'contract_of_sale':
                    qs = qs.filter(service__title='contract_of_sale')
                    context.update(applications=qs)
            if request.GET.get('person_type'):
                qs = qs.filter(person_type=request.GET.get('person_type'))
                context.update(applications=qs)
            if request.GET.get('process'):
                qs = qs.filter(process=request.GET.get('process'))
                context.update(applications=qs)
            if request.GET.get('payment'):
                qs = qs.filter(is_payment=request.GET.get('payment'))
                context.update(applications=qs)
            if request.GET.get('technical'):
                qs = qs.filter(service__car__is_confirm=request.GET.get('technical'))
                context.update(applications=qs)
            if request.GET.get('date'):
                today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
                today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
                some_day_last_week = datetime.datetime.combine(timezone.now().date() - datetime.timedelta(days=7),datetime.time.min)
                some_day_last_month = datetime.datetime.combine(today_min.replace(day=1),datetime.time.min)
                some_day_last_year = datetime.datetime.combine(today_min.replace(month=1, day=1), datetime.time.min)

                if request.GET.get('date') == 'today':
                    qs = qs.filter(created_date__range=(today_min, today_max))
                    context.update(applications=qs)
                if request.GET.get('date') == 'last-7-days':
                    qs = qs.filter(created_date__range=(some_day_last_week, today_max))
                    context.update(applications=qs)
                if request.GET.get('date') == 'month':
                    qs = qs.filter(created_date__range=(some_day_last_month, today_max))
                    context.update(applications=qs)
                if request.GET.get('date') == 'year':
                    qs = qs.filter(created_date__range=(some_day_last_year, today_max))
                    context.update(applications=qs)
        context.update(applications=qs)

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

    payments = calculation_state_duty_service_price(application.service)

    context = {
        'application': application,
        'payments': payments
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
    if service.title == 'account_statement':
        if service.organization:
            doc = DocxTemplate(f"static{os.sep}online{os.sep}account_statement{os.sep}account_statement_legal.docx")
        else:
            doc = DocxTemplate(f"static{os.sep}online{os.sep}account_statement{os.sep}account_statement_person.docx")
    elif service.title == 'gift_agreement':
        if service.organization:
            doc = DocxTemplate(f"static{os.sep}online{os.sep}gift_agreement{os.sep}gift_agreement_legal.docx")
        else:
            doc = DocxTemplate(
                f"static{os.sep}online{os.sep}gift_agreement{os.sep}gift_agreement_person.docx")
    elif service.title == 'contract_of_sale':
        if service.organization:
            doc = DocxTemplate(f"static{os.sep}online{os.sep}contract_of_sale{os.sep}contract_of_sale_legal.docx")
        else:
            doc = DocxTemplate(
                f"static{os.sep}online{os.sep}contract_of_sale{os.sep}contract_of_sale_person.docx")

    car = get_object_or_404(Car, id=service.car.id)

    devices_string = ', '.join([str(i).replace('"', "'") for i in car.device.all()])
    fuel_types_string = ', '.join([str(i).replace('"', "'") for i in car.fuel_type.all()])

    if service.organization:
        context.update(org=service.organization)
    context.update(now_date=datetime.datetime.strftime(timezone.now(), '%d.%m.%Y'),
                   devices=devices_string,
                   fuel_types=fuel_types_string,
                   car=car,
                   state=f"{service.seriya} {datetime.datetime.strftime(service.contract_date, '%d.%m.%Y')}",
                   user=request.user,
                   birthday=datetime.datetime.strftime(request.user.birthday, '%d.%m.%Y'),
                   given_number=car.given_number,
                   old_number=car.old_number,
                   old_technical_passport=car.old_technical_passport
                   )

    car_model = get_object_or_404(CarModel, id=car.model.id)

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
    context = {
        'service': service
    }
    return render(request, 'service/view_service_data.html', context)



@login_required
def change_get_request(request, key, value):
    try:
        url = str(request.META['HTTP_REFERER']).split('?', 1)[0]
        if value == 'all':
            get_params = str(request.META['HTTP_REFERER']).split('?', 1)[1]
            query_dict = {}
            try:
                for par in str(get_params).split('&'):
                    k, v = par.split('=')
                    if key == k:
                        continue
                    query_dict[k] = v

                query = '&'.join([*['{}={}'.format(k, v) for k, v in query_dict.items()]])
                if query == '':
                    return HttpResponseRedirect(url)
                return HttpResponseRedirect(url + '?' + query)
            except ValueError:
                return HttpResponseRedirect(url)
        else:
            get_params = str(request.META['HTTP_REFERER']).split('?', 1)[1]
            query_dict = {}
            try:
                for par in str(get_params).split('&'):
                    k, v = par.split('=')
                    if key == k:
                        continue
                    query_dict[k] = v
                query = '&'.join([f'{key}={value}', *['{}={}'.format(k, v) for k, v in query_dict.items()]])
                if query == '':
                    return HttpResponseRedirect(url)
                return HttpResponseRedirect(url + '?' + query)
            except ValueError:
                return HttpResponseRedirect(url)

    except IndexError:
        # mavjud emas
        url = str(request.META['HTTP_REFERER']).split('?', 1)[0]
        if value == 'all':
            return HttpResponseRedirect(url)
        return HttpResponseRedirect(url + f"?{key}={value}")



