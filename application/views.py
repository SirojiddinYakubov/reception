from base64 import decodestring
from datetime import timezone, datetime, timedelta
from datetime import datetime as dt
import datetime
import json
import os
import random


import pytz
import requests
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
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from application.models import *
from reception.settings import BASE_DIR, SMS_LOGIN, SMS_TOKEN, LOCAL_TIMEZONE
from service.models import StateDuty, STATE_DUTY_TITLE
from service.utils import calculation_state_duty_service_price
from user.models import *
from user.utils import render_to_pdf


@login_required
def applications_list(request):
    applications = Application.objects.filter(Q(is_active=True) & Q(process__in=['1','3']))

    for application in applications:

        #Rad etilgan ariza 30 kundan so'ng o'chirib yuboriladi
        if application.process == '3' and not application.is_block and timezone.now() - timedelta(days=30) > application.created_date:
            application.delete()






    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))
    context = {}

    if request.user.role == '2' or request.user.role == '3':
        region = request.user.section.region
        districts = request.user.section.district.all()

        qs = Application.objects.filter(Q(Q(created_user__region=region) & Q(created_user__district__in=districts) & Q(
            service__organization__isnull=True)) | Q(
            Q(service__organization__legal_address_region=region) & Q(
                service__organization__legal_address_district__in=districts) & Q(
                service__organization__isnull=False))).filter(Q(is_active=True) & Q(is_block=False))
        template = 'user/role/controller/controller_applications_list.html'
    elif request.user.role == '4' or request.user.role == '5':
        region = request.user.section.region
        districts = request.user.section.district.all()

        qs = Application.objects.filter(Q(Q(created_user__region=region) & Q(created_user__district__in=districts) & Q(
            service__organization__isnull=True)) | Q(
            Q(service__organization__legal_address_region=region) & Q(
                service__organization__legal_address_district__in=districts) & Q(
                service__organization__isnull=False))).filter(Q(is_active=True) & Q(is_block=False))
        template = 'user/role/technical/technical_applications_list.html'
    else:
        qs = Application.objects.filter(Q(is_active=True) & Q(created_user=request.user))
        template = 'application/applications_list.html'

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
            if request.GET.get('service') == 'replace_tp':
                qs = qs.filter(service__title='replace_tp')
                context.update(applications=qs)
            if request.GET.get('service') == 'replace_number_and_tp':
                qs = qs.filter(service__title='replace_number_and_tp')
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
        if request.GET.get('confirm'):
            qs = qs.filter(service__car__is_confirm=request.GET.get('confirm'))
            context.update(applications=qs)
        if request.GET.get('technical_confirm'):
            qs = qs.filter(service__car__is_technical_confirm=request.GET.get('technical_confirm'))
            context.update(applications=qs)
        if request.GET.get('date'):
            today_min = datetime.datetime.combine(datetime.date.today(), datetime.time.min)
            today_max = datetime.datetime.combine(datetime.date.today(), datetime.time.max)
            some_day_last_week = datetime.datetime.combine(timezone.now().date() - datetime.timedelta(days=7),
                                                           datetime.time.min)
            some_day_last_month = datetime.datetime.combine(today_min.replace(day=1), datetime.time.min)
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

    if not qs.exists():
        messages.error(request, "Arizalar mavjud emas!")
    return render(request, template, context)


@login_required
def application_detail(request, id):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    application = get_object_or_404(Application, id=id)

    if not request.user.role == '2' or request.user.role == '3' or request.user.role == '4':
        if application.created_user != request.user:
            return redirect(reverse_lazy('application:applications_list'))

    payments = StateDuty.objects.filter(service=application.service)
    if not payments.exists():
        calculation_state_duty_service_price(application.service)

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

    if request.user.role == '1':
        section = Section.objects.get(region=request.user.region, district=request.user.district)
    else:
        section = Section.objects.get(id=request.user.section.id)

    import qrcode
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(f'{request.META["HTTP_HOST"]}{os.sep}application{os.sep}application-detail{os.sep}{application.id}{os.sep}?password={application.password}')
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    if request.META['HTTP_HOST'] == '127.0.0.1:8000':
        img.save(f'media{os.sep}applications{os.sep}qrcodes{os.sep}{application.id}.jpg')
        img_path = f'H:{os.sep}django_projects{os.sep}reception{os.sep}media{os.sep}applications{os.sep}qrcodes{os.sep}{application.id}.jpg'
    else:
        img.save(f'{os.sep}home{os.sep}pyth{os.sep}reception{os.sep}media{os.sep}applications{os.sep}qrcodes{os.sep}{application.id}.jpg')
        img_path = f"{os.sep}home{os.sep}pyth{os.sep}reception{os.sep}media{os.sep}applications{os.sep}qrcodes{os.sep}{application.id}.jpg"


    context = {
        'now_date': datetime.datetime.strftime(timezone.now(), '%d.%m.%Y'),
        'created_date': datetime.datetime.strftime(application.created_date, '%d.%m.%Y'),
        'app': application,
        'section': section,
        'img_path': img_path
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
        # account_statement = get_object_or_404(AccountStatement, id=application.account_statement.id)

        context = {
            'user': f"{user.last_name} {user.first_name}",
            # 'account_statement_photo_url': account_statement.cert_photo.url
        }

        data = json.dumps(context)
        return HttpResponse(data, content_type='json')
    else:
        return False


@login_required
def create_application_doc(request, filename):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    application = get_object_or_404(Application, file_name=filename)

    if application.is_block:
        messages.error(request, 'Ariza nusxasini yuklab olish uchun arizani faollashtirishingiz talab etiladi!')
        return redirect(reverse_lazy('application:application_detail', kwargs={'id': application.id}))
    service = get_object_or_404(Service, id=application.service.id)
    if request.user.role == '1':
        section = Section.objects.get(region=request.user.region, district=request.user.district)
    else:
        section = Section.objects.get(id=request.user.section.id)

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
    elif service.title == 'replace_tp':
        if service.organization:
            doc = DocxTemplate(f"static{os.sep}online{os.sep}replace_tp{os.sep}replace_tp_legal.docx")
        else:
            doc = DocxTemplate(
                f"static{os.sep}online{os.sep}replace_tp{os.sep}replace_tp_person.docx")
    elif service.title == 'replace_number_and_tp':
        if service.organization:
            doc = DocxTemplate(
                f"static{os.sep}online{os.sep}replace_number_and_tp{os.sep}replace_number_and_tp_legal.docx")
        else:
            doc = DocxTemplate(
                f"static{os.sep}online{os.sep}replace_number_and_tp{os.sep}replace_number_and_tp_person.docx")
    elif service.title == 're_equipment':
        if service.organization:
            doc = DocxTemplate(f"static{os.sep}online{os.sep}re_equipment{os.sep}re_equipment_legal.docx")
        else:
            doc = DocxTemplate(
                f"static{os.sep}online{os.sep}re_equipment{os.sep}re_equipment_person.docx")

    car = get_object_or_404(Car, id=service.car.id)

    devices_string = ', '.join([str(i).replace('"', "'") for i in car.device.all()])
    fuel_types_string = ', '.join([str(i).replace('"', "'") for i in car.fuel_type.all()])
    re_fuel_types_string = ', '.join([str(i).replace('"', "'") for i in car.re_fuel_type.all()])

    if service.seriya and service.contract_date:
        context.update(state=f"{service.seriya} {service.contract_date.strftime('%d.%m.%Y')}")

    if car.given_technical_passport:
        context.update(given_technical_passport=car.given_technical_passport)
    if service.organization:
        context.update(org=service.organization)
        context.update(
            legal_address=f"{service.organization.legal_address_region.title}, {service.organization.legal_address_district.title}")
    context.update(now_date=datetime.datetime.strftime(timezone.now(), '%d.%m.%Y'),
                   devices=devices_string,
                   fuel_types=fuel_types_string,
                   car=car,
                   made_year=car.made_year.strftime("%d.%m.%Y"),
                   user=application.created_user,
                   birthday=application.created_user.birthday.strftime('%d.%m.%Y'),
                   given_number=car.given_number,
                   old_number=car.old_number,
                   old_technical_passport=car.old_technical_passport,
                   re_fuel_types=re_fuel_types_string,
                   section=section)

    car_model = get_object_or_404(CarModel, id=car.model.id)

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


@login_required
def view_service_data(request, service_id):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    service = get_object_or_404(Service, id=service_id)
    application = get_object_or_404(Application, id=service.application_service.all().first().id)
    if request.user.role == '1' and application.created_user != request.user:
        return render(request, '_parts/404.html')

    context = {
        'service': service
    }
    return render(request, 'service/view_service_data.html', context)


@login_required
def change_get_request(request, key, value):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

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


@permission_classes([IsAuthenticated])
class ConfirmApplicationData(APIView):
    def post(self, request):
        application = get_object_or_404(Application, id=request.POST.get('application'))
        car = get_object_or_404(Car, id=application.service.car.id)
        if request.user.role == '1':
            return HttpResponse(False)

        if request.is_ajax():
            if request.method == 'POST':
                if request.POST.get('process') == 'confirm':
                    car.given_number = request.POST.get('given_number')
                    car.given_technical_passport = request.POST.get('technical_passport')
                    car.save()
                    application.process_sms = 'Muvaffaqiyatli tasdiqlandi!'
                    application.process = '2'
                    application.given_date = datetime.datetime.strptime(request.POST.get('given_date'),
                                                                        "%Y-%m-%d").date()
                    application.given_time = request.POST.get('given_time')
                    application.save()

                    msg = f"Hurmatli foydalanuvchi! {application.id}-raqamli arizangiz muvvaffaqiyatli tasdiqlandi!%0a{car.given_technical_passport} seriya va raqamli qayd etish guvohnomasi{' va {0} davlat raqam belgisini'.format(car.given_number) if car.given_number else 'ni'} {application.given_date.strftime('%d.%m.%Y') + '-yil'} {request.POST.get('given_time')} da {request.user.section.title} ga kelib olib ketishingizni so'raymiz."
                    msg = msg.replace(" ", "+")
                    url = f"https://developer.apix.uz/index.php?app=ws&u={SMS_LOGIN}&h={SMS_TOKEN}&op=pv&to=998{application.created_user.phone}&msg={msg}"
                    response = requests.get(url)
                    return HttpResponse(True)
                elif request.POST.get('process') == 'cancel':
                    application.process = '3'
                    application.process_sms = request.POST.get('process_sms')
                    application.canceled_date = timezone.now()
                    application.save()

                    msg = f"Hurmatli foydalanuvchi! {application.id}-raqamli arizangiz {request.POST.get('process_sms')} bekor qilindi! {request.user.section.title}"
                    msg = msg.replace(" ", "+")
                    url = f"https://developer.apix.uz/index.php?app=ws&u={SMS_LOGIN}&h={SMS_TOKEN}&op=pv&to=998{application.created_user.phone}&msg={msg}"
                    response = requests.get(url)
                    return HttpResponse(True)
                elif request.POST.get('process') == 'process':
                    application.process = '1'
                    application.process_sms = request.POST.get('process_sms')
                    application.save()

                    msg = f"Hurmatli foydalanuvchi! {application.id}-raqamli arizangiz {request.POST.get('process_sms')} jarayonda turibti! {request.user.section.title}"
                    msg = msg.replace(" ", "+")
                    url = f"https://developer.apix.uz/index.php?app=ws&u={SMS_LOGIN}&h={SMS_TOKEN}&op=pv&to=998{application.created_user.phone}&msg={msg}"
                    response = requests.get(url)
                    return HttpResponse(True)
                else:
                    return HttpResponse(False)
            else:
                return HttpResponse(False)
        else:
            return HttpResponse(False)


@permission_classes([IsAuthenticated])
class GetGivenNumber(APIView):
    def post(self, request, id):
        application = get_object_or_404(Application, id=id)
        car = get_object_or_404(Car, id=application.service.car.id)
        if car.is_auction:
            if car.given_number:
                return HttpResponse(car.given_number)
            else:
                return HttpResponse('')
        else:
            return HttpResponse('')


@permission_classes([IsAuthenticated])
class RemoveApplication(APIView):
    def post(self, request):
        application = Application.objects.filter(id=request.POST.get('application')).first()

        if application:
            if application.service.car.is_confirm or application.is_payment or application.process == '2':
                return HttpResponse('disabled')
            else:
                application.delete()
                return HttpResponse(True)
        else:
            return HttpResponse(False)


@login_required
def payment_detail(request, service_id):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    service = get_object_or_404(Service, id=service_id)
    application = get_object_or_404(Application, id=service.application_service.all().first().id)
    payments = StateDuty.objects.filter(service=service, is_active=True)
    if request.user.role == '1':
        section = Section.objects.get(region=request.user.region, district=request.user.district)
    else:
        section = Section.objects.get(id=request.user.section.id)

    if (request.user.role == '1' and application.created_user != request.user) or (
            (request.user.role == '2' or request.user.role == '3') and (request.user.section != section)):
        return render(request, '_parts/404.html')

    context = {
        'service': service,
        'payments': payments
    }
    return render(request, 'application/payments/payment_detail.html', context)


@login_required
def payments(request):
    if request.user.role == '2' or request.user.role == '3':
        region = request.user.section.region
        districts_list = request.user.section.district.all()

        # services = Service.objects.filter(Q(Q(application_service__created_user__region=region) & Q(
        #     application_service__created_user__district__in=districts_list) & Q(
        #     organization__isnull=True)) | Q(
        #     Q(organization__legal_address_region=region) & Q(organization__legal_address_district__in=districts_list) & Q(
        #         organization__isnull=False))).filter(
        #     Q(application_service__is_active=True) & Q(application_service__is_block=False))

        context = {
            'region': region,
            'districts_list': districts_list,
            'pays': STATE_DUTY_TITLE
        }

        # startdate = timezone.now().replace(year=2021,month=1,day=1)
        # stopdate = timezone.now()
        # stopdate = datetime.datetime.now().replace(tzinfo=LOCAL_TIMEZONE)

        if request.method == 'GET':
            try:
                if request.GET.get('startdate') and request.GET.get('startdate') != 'None' and request.GET.get('startdate') != '':
                    # startdate = dt.strptime(request.GET.get('startdate'), "%Y-%m-%d").replace(tzinfo=LOCAL_TIMEZONE)
                    context.update(startdate=request.GET.get('startdate'))
                if request.GET.get('stopdate') and request.GET.get('stopdate') != 'None' and request.GET.get('stopdate') != '':
                    # stopdate = dt.strptime(request.GET.get('stopdate'), '%Y-%m-%d').replace(tzinfo=LOCAL_TIMEZONE, hour=23,minute=59,second=59)
                    context.update(stopdate=request.GET.get('stopdate'))
                # if request.GET.get('district') and request.GET.get('district') != 'all':
                #     districts = District.objects.filter(id=request.GET.get('district'))
                #     context.update(districts=districts)
                # else:
                #     context.update(districts=districts_list)
            except:
                messages.error(request, 'Xatolik yuz berdi! Sanani tanlashda xatolik!')
                return render(request, 'application/payments/payments.html', context)
        # payments = StateDuty.objects.filter(Q(is_active=True) & Q(service__in=services) & Q(created_date__range=[startdate, stopdate]))
        # context.update(payments=payments)
        return render(request, 'application/payments/payments.html', context)
    else:
        return render(request, '_parts/404.html')


@permission_classes([IsAuthenticated])
class Modify_Payment_Checkbox(APIView):
    def post(self, request):
        try:
            if request.user.role == '2' or request.user.role == '3':
                get_payment = request.POST.get('payment')
                modify = request.POST.get('modify')

                if modify == 'true':
                    modify = True
                else:
                    modify = False

                payment = StateDuty.objects.get(id=get_payment)
                if payment:
                    payment.is_paid = modify

                    service = Service.objects.get(id=payment.service.id)
                    if service:
                        application = Application.objects.get(id=service.application_service.first().id)
                        if application:
                            payments = StateDuty.objects.filter(service=service)
                            if payments.exists():
                                payment.save()
                                if all(payment.is_paid for payment in payments):
                                    application.is_payment = True
                                    application.save()
                                else:
                                    application.is_payment = False
                                    application.save()

                                return HttpResponse(True)
                            else:
                                return HttpResponse(False)
                        else:
                            return HttpResponse(False)
                    else:
                        return HttpResponse(False)
                else:
                    return HttpResponse(False)
            else:
                return HttpResponse(False)
        except:
            return HttpResponse(False)
