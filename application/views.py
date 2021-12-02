from datetime import timezone, datetime
from itertools import chain

from django.contrib import messages
from django.contrib.humanize.templatetags.humanize import naturalday
from django.views.generic import DetailView
from docxtpl import DocxTemplate
from reportlab.pdfgen import canvas
from requests import Response
from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from application.generators import *
from application.mixins import *
from application.models import *
from application.permissions import allowed_users
from application.serializers import DocumentForPoliceSerializer, SaveDraftApplicationSerializer
from application.utils import filter_state_duty_percents
from reception.api import SendSmsWithApi, SendSmsWithPlayMobile
from reception.mixins import *
from reception.settings import *
from reception.telegram_bot import send_message_to_developer
from service.models import *
from user.models import *
from user.utils import render_to_pdf


class ApplicationsList(ApplicationCustomMixin, AllowedRolesMixin):
    template_name = 'application/applications_list.html'
    allowed_roles = [USER, CHECKER, REVIEWER, TECHNICAL, SECTION_CONTROLLER, REGIONAL_CONTROLLER, STATE_CONTROLLER,
                     MODERATOR, ADMINISTRATOR, SUPER_ADMINISTRATOR, APP_CREATOR]

    def get_template_names(self):
        role = self.request.user.role
        if role == CHECKER:
            return ['user/role/checker/checker_applications_list.html']
        elif role == REGIONAL_CONTROLLER:
            return ['user/role/regional_controller/applications_list.html']
        elif role == MODERATOR:
            return ['user/role/moderator/applications_list.html']
        return [self.template_name]

    def get_queryset(self):
        role = self.request.user.role
        qs = super().get_queryset().filter(is_active=True)
        if role == CHECKER:
            section = get_object_or_404(Section, id=self.request.user.section.id)
            qs = qs.filter(section=section, is_block=False).filter(
                process__in=[SHIPPED, ACCEPTED_FOR_CONSIDERATION, WAITING_FOR_PAYMENT, WAITING_FOR_ORIGINAL_DOCUMENTS,
                             ACCEPTED, REJECTED])
        elif role == APP_CREATOR:
            qs = qs.filter(created_user=self.request.user)
        elif role == USER:
            qs = qs.filter(Q(created_user=self.request.user) | Q(applicant=self.request.user)).distinct()
        elif role == REGIONAL_CONTROLLER:
            qs = qs.filter(section__region=self.request.user.region, is_block=False).filter(
                process__in=[SHIPPED, ACCEPTED_FOR_CONSIDERATION, WAITING_FOR_PAYMENT, WAITING_FOR_ORIGINAL_DOCUMENTS,
                             ACCEPTED, REJECTED])
        elif role == MODERATOR:
            qs = qs
        return qs

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return super().get_json_data()
        else:
            return super().get(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context.update(application=)
    #     return context


class ApplicationDetail(AllowedRolesMixin, DetailView):
    model = Application
    template_name = 'application/application_detail.html'
    pk_url_kwarg = 'id'
    allowed_roles = [USER, CHECKER, REVIEWER, TECHNICAL, SECTION_CONTROLLER, REGIONAL_CONTROLLER, STATE_CONTROLLER,
                     MODERATOR, ADMINISTRATOR, SUPER_ADMINISTRATOR, APP_CREATOR]

    def get(self, request, *args, **kwargs):
        application = get_object_or_404(Application, id=self.kwargs['id'])

        if request.user.role == USER:
            if application.created_user == request.user:
                return super().get(request, *args, **kwargs)
            return redirect(reverse_lazy('error_403'))
        elif request.user.role == CHECKER:
            return super().get(request, *args, **kwargs)
        elif request.user.role == APP_CREATOR:
            if request.user == application.created_user:
                return super().get(request, *args, **kwargs)
            return redirect(reverse_lazy('error_403'))

    def get_context_data(self, **kwargs):
        application = get_object_or_404(Application, id=self.kwargs['id'])
        percents = filter_state_duty_percents(application)

        context = {
            'application': application,
            'percents': percents,
        }

        if AmountBaseCalculation.objects.filter(is_active=True):
            activation_pay = int(AmountBaseCalculation.objects.filter(is_active=True).last().amount * 5 / 100)
            context.update(activation_pay=activation_pay)
        return context


def generate_qr_code_image(request, id):
    try:
        application = get_object_or_404(Application, id=id)
        link = create_link(request, application.id)
        qr = create_qr_code(link, 10, 2)
        response = HttpResponse(content_type="image/png")
        qr.save(response, "PNG")
        return response
    except:
        return HttpResponse('APPLICATION NOT FOUND')


class ApplicationPdf(AllowedRolesMixin, View):
    template_name = 'application/application_detail_pdf.html'
    pk_url_kwarg = 'id'
    allowed_roles = [USER, CHECKER, REVIEWER, TECHNICAL, SECTION_CONTROLLER, REGIONAL_CONTROLLER, STATE_CONTROLLER,
                     MODERATOR, ADMINISTRATOR, SUPER_ADMINISTRATOR]

    def get(self, request, *args, **kwargs):
        application = get_object_or_404(Application, id=self.kwargs[self.pk_url_kwarg])
        pdf = render_to_pdf(self.template_name, self.get_context_data())
        p = canvas.Canvas(pdf)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Ariza #%s.pdf" % (application.id)
            content = "attachment; filename=%s" % (filename)
            response['Content-Disposition'] = content
            return response

    def get_context_data(self, *args, **kwargs):
        application = get_object_or_404(Application, id=self.kwargs[self.pk_url_kwarg])

        context = {
            'now_date': timezone.now(),
            'created_date': application.created_date,
            'app': application,
            'section': application.section,
            'request': self.request,
        }
        return context

    def create_password(self):
        from PyPDF2 import PdfFileReader, PdfFileWriter
        with open('test.pdf', 'rb') as inputfile:
            # Load PDF file from file
            pdf_reader = PdfFileReader(inputfile)
            pdf_writer = PdfFileWriter()
            # Number of pages
            num_pages = pdf_reader.getNumPages()
            for page in range(num_pages):
                pdf_writer.addPage(pdf_reader.getPage(page))
            user_password = "PASSSWORD"
            pdf_writer.encrypt(user_password, "password", )

            with open("print-enable-with-pass.pdf", "wb") as outputfile:
                pdf_writer.write(outputfile)


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
    application = Application.objects.get(file_name=filename)

    if application.process == DRAFT:
        messages.error(request, 'Ariza nusxasini yuklab olish uchun arizani to\'liq to\'ldiring!')
        return redirect(reverse_lazy('application:application_detail', kwargs={'id': application.id}))
    section = Section.objects.get(id=application.section.id)

    if application.is_block:
        messages.error(request, 'Ariza nusxasini yuklab olish uchun arizani faollashtirishingiz talab etiladi!')
        return redirect(reverse_lazy('application:application_detail', kwargs={'id': application.id}))

    service = Service.objects.get(id=application.service.id)

    context = {}
    if application.organization:
        doc = DocxTemplate(f"static{os.sep}online{os.sep}{service.key}{os.sep}{service.key}_legal.docx")
    else:
        doc = DocxTemplate(f"static{os.sep}online{os.sep}{service.key}{os.sep}{service.key}_person.docx")

    car = get_object_or_404(Car, id=application.car.id)

    devices_string = ', '.join([str(i).replace('"', "'") for i in car.device.all()])
    fuel_types_string = ', '.join([str(i).replace('"', "'") for i in car.fuel_type.all()])
    re_fuel_type_string = car.re_fuel_type.title if car.re_fuel_type else ''

    application_document = ApplicationDocument.objects.filter(example_document__key=service.key,
                                                              application=application).last()

    if application_document and application_document.contract_date:
        context.update(state=f"{application_document.seriya} {application_document.contract_date.strftime('%d.%m.%Y')}")

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
                   user=application.created_user,
                   birthday=application.created_user.birthday.strftime('%d.%m.%Y'),
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


@login_required
def view_service_data(request, service_id):
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
        print('key' + key + ' ,value: ' + value)
        return HttpResponseRedirect(url + f"?{key}={value}")


class ConfirmApplicationData(APIView, AllowedRolesMixin):
    allowed_roles = [CHECKER, REVIEWER, SECTION_CONTROLLER, REGIONAL_CONTROLLER, STATE_CONTROLLER,
                     MODERATOR, ADMINISTRATOR, SUPER_ADMINISTRATOR]

    def post(self, request):
        try:
            application = get_object_or_404(Application, id=request.POST.get('application'))
            car = get_object_or_404(Car, id=application.car.id)

            if request.is_ajax():
                if request.method == 'POST':

                    if request.POST.get('process') == 'confirm':
                        # car.given_number = request.POST.get('given_number')
                        # car.given_technical_passport = request.POST.get('technical_passport')
                        # car.save()

                        application.process = ACCEPTED
                        # application.given_date = datetime.datetime.strptime(request.POST.get('given_date'),
                        #                                                     "%Y-%m-%d").date()
                        # application.given_time = request.POST.get('given_time')
                        application.inspector = request.user
                        application.confirmed_date = timezone.now()
                        application.save()

                        # text = f"Hurmatli foydalanuvchi! {application.id}-raqamli arizangiz muvvaffaqiyatli tasdiqlandi! {car.given_technical_passport} seriya va raqamli qayd etish guvohnomasi{' va {0} davlat raqam belgisini'.format(car.given_number) if car.given_number else 'ni'} {application.given_date.strftime('%d.%m.%Y') + '-yil'} {request.POST.get('given_time')} da {request.user.section.region.title} {request.user.section.title} ga kelib olib ketishingizni so'raymiz. Qo'shimcha ma'lumot uchun tel:972800809"
                        # text = f"Hurmatli foydalanuvchi! {application.id}-raqamli arizangiz muvvaffaqiyatli tasdiqlandi! {application.given_date.strftime('%d.%m.%Y') + '-yil'} {request.POST.get('given_time')} da {request.user.section.region.title} {request.user.section.title} ga kelib olib ketishingizni so'raymiz. Qo'shimcha ma'lumot uchun tel:972800809"
                        text = f"Hurmatli foydalanuvchi! {application.id}-raqamli arizangiz muvvaffaqiyatli tasdiqlandi! {request.user.section.region.title} {request.user.section.title} ga kelib qayd etish guvohnomasini olib ketishingizni so'raymiz. Qo'shimcha ma'lumot uchun tel:972800809"

                        # create notification
                        notification = Notification.objects.create(application=application, sender=request.user,
                                                                   receiver=application.created_user, text=text)
                        r = SendSmsWithPlayMobile(phone=application.created_user.phone, message=text).get()
                        print(text)
                        if not r == SUCCESS:
                            # send sms with eskiz
                            r = SendSmsWithApi(phone=application.created_user.phone, message=text).get()
                        if r != SUCCESS:
                            send_message_to_developer(f'Sms service not working! Notification: {notification}')
                        return HttpResponse(status=200)
                    elif request.POST.get('process') == 'cancel':
                        application.process = REJECTED
                        application.canceled_date = timezone.now()
                        application.inspector = request.user
                        application.save()

                        text = f"Hurmatli foydalanuvchi! {application.id}-raqamli arizangiz rad etildi! Rad etish sababi: {request.POST.get('process_sms')}! YHXB RIB bo'limi: {request.user.section.region.title} {request.user.section.title}, Qo'shimcha ma'lumot uchun tel:972800809"

                        # create notification
                        notification = Notification.objects.create(application=application, sender=request.user,
                                                                   receiver=application.created_user, text=text)

                        r = SendSmsWithPlayMobile(phone=application.created_user.phone, message=text).get()
                        print(text)
                        if not r == SUCCESS:
                            # send sms with eskiz
                            r = SendSmsWithApi(phone=application.created_user.phone, message=text).get()

                        if r != SUCCESS:
                            send_message_to_developer(f'Sms service not working! Notification: {notification}')
                        return HttpResponse(status=200)
                    elif request.POST.get('process') == 'process':

                        application.process = ACCEPTED_FOR_CONSIDERATION
                        application.inspector = request.user
                        application.save()

                        text = f"Hurmatli foydalanuvchi! {application.id}-raqamli arizangiz {request.user.section.region.title} {request.user.section.title} tomonidan ko'rib chiqish uchun qabul qilindi! Kerakli hisob raqamlarga to'lovlarni amalga oshirib, transport vositasini texnik ko'rik va ma'lumotlar mosligini tasdiqlatgandan so'ng hujjatlarning asl nusxasini {request.user.section.region.title} {request.user.section.title} ga keltirib topshirishingizni so'raymiz! Qo'shimcha ma'lumot uchun tel:972800809"

                        # create notification
                        notification = Notification.objects.create(application=application, sender=request.user,
                                                                   receiver=application.created_user, text=text)

                        r = SendSmsWithPlayMobile(phone=application.created_user.phone, message=text).get()
                        print(text)
                        if not r == SUCCESS:
                            # send sms with eskiz
                            r = SendSmsWithApi(phone=application.created_user.phone, message=text).get()

                        if r != SUCCESS:
                            send_message_to_developer(f'Sms service not working! Notification: {notification}')
                        if r != SUCCESS:
                            send_message_to_developer(f'Sms service not working! Notification: {notification}')
                        return HttpResponse(status=200)
                    else:
                        HttpResponse(status=404)
                else:
                    HttpResponse(status=404)
            else:
                HttpResponse(status=404)
        except Exception as e:
            print(e)
            return HttpResponse(status=404)


class GetGivenNumber(APIView, AllowedRolesMixin):
    allowed_roles = [USER, CHECKER, REVIEWER, TECHNICAL, SECTION_CONTROLLER, REGIONAL_CONTROLLER, STATE_CONTROLLER,
                     MODERATOR, ADMINISTRATOR, SUPER_ADMINISTRATOR]

    def post(self, request, id):
        try:
            application = get_object_or_404(Application, id=id)
            car = get_object_or_404(Car, id=application.car.id)
            if car.is_auction:
                if car.given_number:
                    return HttpResponse(car.given_number, status=200)
                else:
                    return HttpResponse(status=200)
            else:
                return HttpResponse(status=200)
        except:
            return HttpResponse(status=404)


@permission_classes([IsAuthenticated])
class RemoveApplication(APIView):
    def post(self, request):
        application = Application.objects.filter(id=request.POST.get('application')).first()

        if application:
            if application.service.car.is_confirm or application.is_payment or application.process == '2':
                return HttpResponse('disabled')
            else:
                print('delete')
                # application.delete()
                return HttpResponse(True)
        else:
            return HttpResponse(False)


@login_required
def payment_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)
    application = get_object_or_404(Application, id=service.application_service.all().first().id)
    payments = PaidStateDuty.objects.filter(service=service, is_active=True)
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


class PaymentsList(AllowedRolesMixin, ListView):
    model = PaidStateDuty
    template_name = 'application/payments/payments_list.html'
    allowed_roles = [USER, CHECKER, SECTION_CONTROLLER, REGIONAL_CONTROLLER, STATE_CONTROLLER, MODERATOR, ADMINISTRATOR,
                     SUPER_ADMINISTRATOR]

    def get_template_names(self):
        role = self.request.user.role
        if role == USER:
            return ['application/payments/user_payments_list.html']
        return [self.template_name]

    def get_context_data(self, **kwargs):
        user_role = self.request.user.role

        context = {
            'pays': STATE_DUTY_TITLE
        }

        if user_role == STATE_CONTROLLER:
            if self.request.method == 'GET':
                try:
                    if self.request.GET.get('startdate', None):
                        context.update(startdate=self.request.GET.get('startdate'))
                    if self.request.GET.get('stopdate', None):
                        context.update(stopdate=self.request.GET.get('stopdate'))
                except:
                    pass

            parent_sections = Section.objects.filter(parent__isnull=True)
            context.update(parent_sections=parent_sections)

            if self.request.GET.get('parent_section', None):
                if self.request.GET.get('parent_section').isdigit():
                    parent_section = get_object_or_404(Section, id=self.request.GET.get('parent_section'))
                    child_sections = Section.objects.filter(parent=parent_section)
                    context.update(child_sections=child_sections)
        elif user_role == USER:
            applications = Application.objects.filter(is_active=True)
            context.update(applications=applications)

        return context


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

                payment = PaidStateDuty.objects.get(id=get_payment)
                if payment:
                    payment.is_paid = modify
                    service = Service.objects.get(id=payment.service.id)
                    if service:
                        application = Application.objects.get(id=service.application_service.first().id)
                        if application:
                            payments = PaidStateDuty.objects.filter(service=service)
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


def check_application_status(request, id):
    application = get_object_or_404(Application, id=id)
    payments = PaidStateDuty.objects.filter(service=application.service)

    context = {
        'application': application,
        'payments': payments
    }
    return render(request, 'application/check_application_status.html', context)


def access_with_qrcode(request, id):
    application = get_object_or_404(Application, id=id)
    print('welcome')
    print(application)
    return None


class SectionApplicationsList(ApplicationCustomMixin, AllowedRolesMixin):
    model = Application
    template_name = 'application/applications_list.html'
    render_application_values = ['id', 'service', 'service__car', 'service__car__old_number', 'created_user',
                                 'created_date', 'file_name', 'process']
    allowed_roles = [SECTION_CONTROLLER, REGIONAL_CONTROLLER, STATE_CONTROLLER, MODERATOR, ADMINISTRATOR,
                     SUPER_ADMINISTRATOR]

    @allowed_users(allowed_roles=[*allowed_roles])
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            return super().get_json_data()
        else:
            return super().get(request, *args, **kwargs)

    def get_queryset(self):
        section = get_object_or_404(Section, id=self.kwargs['section_id'])
        return super().get_queryset().filter(section=section)

    def get_context_data(self, **kwargs):
        context = dict()
        context['section'] = Section.objects.get(id=self.kwargs['section_id'])
        return context


class SaveApplicationSection(AllowedRolesMixin, View):
    allowed_roles = [USER, CHECKER, SECTION_CONTROLLER, REGIONAL_CONTROLLER, STATE_CONTROLLER, MODERATOR, ADMINISTRATOR,
                     SUPER_ADMINISTRATOR, APP_CREATOR]

    def post(self, request, *args, **kwargs):
        print(request.POST)
        if request.POST.get('section', None) and request.POST.get('application', None):
            section = get_object_or_404(Section, id=request.POST.get('section'))
            application = get_object_or_404(Application, id=request.POST.get('application'))
            application.section = section
            application.process = CREATED
            application.save()
            return HttpResponse(status=200)
        return HttpResponse(status=400)


class DraftToShipped(APIView):
    allowed_roles = [USER, CHECKER, SECTION_CONTROLLER, REGIONAL_CONTROLLER, STATE_CONTROLLER, MODERATOR, ADMINISTRATOR,
                     SUPER_ADMINISTRATOR]

    def post(self, request, *args, **kwargs):
        try:
            application_id = kwargs.get('application_id')
            application = Application.objects.get(id=application_id)
            base_amount = AmountBaseCalculation.objects.filter(is_active=True).last()
            if not base_amount:
                return Response({'error': f"Eng kam oylik ish haqi topilmadi!"}, status=400)

            if application.process == DRAFT:
                return Response({'error': f"Ariza to'liq to'ldirilmagan!"}, status=400)

            if application.is_block:
                return Response({
                    'error': f"Ariza aktivlashtirilmagan! Arizani {application.section.title} ga jo'natish uchun {int(base_amount.amount / 100 * 5)} so'm to'lov qilishingiz kerak",
                },
                    status=400)
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
            return Response(serializer.data, status=200)
        except Exception as e:
            return Response({'error': str(e)}, status=400)


class ApplicationCashByModeratorView(AllowedRolesMixin, View):
    permission_classes(IsAuthenticated, )
    allowed_roles = [USER, MODERATOR, CHECKER]

    def post(self, request, *args, **kwargs):
        if request.POST.get('type') == str(APPLICATION_ACTIVATION):
            if request.POST.get('application') and request.POST.get('secret_key'):
                application = get_object_or_404(Application, id=request.POST.get('application'))
                moderator = get_object_or_404(User, secret_key=request.POST.get('secret_key'),
                                              role__in=self.allowed_roles)
                if not (application.is_block and application.process == CREATED):
                    print('Application status already active')
                    return HttpResponse(status=409)
                application.is_block = False
                application.process = SHIPPED
                application.save()
                ApplicationCashByModerator.objects.create(status=APPLICATION_ACTIVATION, application=application,
                                                          moderator=moderator)
                return HttpResponse(status=200)
        elif request.POST.get('type') == str(APPLICATION_STATE_DUTY_PAYMENT):
            print(request.POST)
            if request.POST.get('application') and request.POST.get('secret_key') and request.POST.get('payment'):
                payment_id = request.POST.get('payment')
                application = get_object_or_404(Application, id=request.POST.get('application'))
                moderator = get_object_or_404(User, secret_key=request.POST.get('secret_key'),
                                              role__in=self.allowed_roles)
                percent = get_object_or_404(StateDutyPercent, id=payment_id)
                try:
                    score = StateDutyScore.objects.get(district=application.created_user.district,
                                                       state_duty=percent.state_duty)
                except:
                    score = StateDutyScore.objects.get(state_duty=percent.state_duty)

                paid_state_duty = PaidStateDuty.objects.filter(application=application, score=score,
                                                               percent=percent).last()

                if paid_state_duty:
                    print('Application payments already paid')
                    return HttpResponse(status=409)
                else:
                    paid_state_duty = PaidStateDuty.objects.create(application=application, score=score,
                                                                   percent=percent)
                    ApplicationCashByModerator.objects.create(status=APPLICATION_STATE_DUTY_PAYMENT,
                                                              application=application, paid_state_duty=paid_state_duty,
                                                              moderator=moderator)
                    # bu yerga agar hamma to'lovlar o'tgan bo'lsa application is_paymentni True qilish kerak
                    return HttpResponse(status=200)
        else:
            return HttpResponse(status=404)
        return HttpResponse(status=404)


class SaveDraftApplication(UpdateAPIView):
    model = Application
    serializer_class = SaveDraftApplicationSerializer
    permission_classes = [IsAuthenticated]

    def patch(self, request, *args, **kwargs):
        print(request)
        return super(SaveDraftApplication, self).patch(*args, **kwargs)
