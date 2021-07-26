import json
import random
from django.contrib.auth.mixins import *
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, user_logged_out, logout
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.db.models import Q
from application.mixins import *
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import RequestContext
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic.base import View
from docxtpl import DocxTemplate
from django.utils.decorators import *
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import permission_classes
from xhtml2pdf import pisa
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import *
from django.views.generic import ListView, DetailView, View
from application.models import Application
from application.utils import application_right_filters
from reception.mixins import *
from reception.settings import *
from reception.prod_settings import LOG_FILE_PATH, logger
from service.models import *
from service.utils import calculation_state_duty_service_price
from user.decorators import *
from user.forms import *
import reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from user.utils import render_to_pdf
from django.utils.translation import ugettext_lazy as _
from django.utils.translation import ugettext as __

@login_required
def personal_data(request):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('landing:home_page'))
    # generate pdf

    # html holatda ekranga chiqarish
    if request.user.person_id == None:
        return redirect(reverse_lazy('user:edit_personal_data'))
    # template = get_template('user/personal_data.html')
    passport = '{} {}'.format(request.user.passport_seriya, request.user.passport_number)
    context = {
        'user': request.user,
        'passport': passport,
        'request': request
    }

    # html = template.render(context)

    return render(request, 'user/personal_data.html', context)


# pdf holatda ekranga chiqarish
# context = {
#     'date': datetime.date.today()
# }
# template_name = 'online/user_information.html'
# pdf = render_to_pdf(template_name, context)
# if pdf:
#     response = HttpResponse(pdf, content_type='application/pdf')
#     filename = "Shahsiy ma'lumot #%s.pdf" %('123')
#     #pdfni ekranda ko'rsatish inline
#     content = "inline; filename=%s" %(filename)
#
#     #dowload
#     download = request.GET.get('download')
#     if download:
#         #pdfni yuklab olish attachment
#         content = "attachment; filename=%s" % (filename)
#     response['Content-Disposition'] = content
#     return response

# return HttpResponse(pdf, content_type='application/pdf')
# return HttpResponse("Ma'lumot topilmadi")


def user_signup(request):
    regions = Region.objects.all()

    context = {
        'regions': regions,
    }
    return render(request, 'account/signup.html', context)


@login_required
def user_logout(request):
    return render(request, 'account/logout.html')


class Logout(APIView):
    def get(self, request, format=None):
        # using Django logout
        logout(request)
        return redirect(reverse_lazy('user:login_view'))


def login_view(request):
    print(request.POST)
    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        next = request.POST.get('next', None)
        if username and password:
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)

                    token, created = Token.objects.get_or_create(user=user)
                    if next:
                        response = HttpResponseRedirect(next)
                    else:
                        response = redirect('service:services_list')
                    response.set_cookie('token', token.key, max_age=TOKEN_MAX_AGE)
                    return response
                else:
                    messages.warning(request, "Sizning profilingiz faol holatda emas!")
                    return redirect('user:login_view')
            else:
                messages.error(request, "Login yoki parol noto'g'ri!")
                return redirect('user:login_view')
        else:
            messages.error(request, "Formani to'ldirishda xatolik!")
            return redirect('user:login_view')
    else:
        return render(request, 'account/login.html')
    # if request.method == 'POST':
    #     phone = request.POST.get('phone', None)
    #     password = request.POST.get('password', '')
    #     context = {
    #         'phone': phone
    #     }
    #     if len(str(phone)) != 9:
    #         try:
    #             phone = request.COOKIES['phone']
    #         except KeyError:
    #             return redirect(reverse_lazy('user:login_view'))
    #     try:
    #         user1 = User.objects.get(username=phone)
    #         if not user1.is_staff and user1.person_id == None:
    #             return redirect(reverse_lazy('user:signup'))
    #         user = authenticate(request, username=phone, password=password)
    #
    #         if user is not None:
    #             login(request, user)
    #             token, created = Token.objects.get_or_create(user=user)
    #             response = redirect(reverse('user:personal_data'))
    #             response.set_cookie('token', token.key, max_age=TOKEN_MAX_AGE)
    #             return response
    #         else:
    #             messages.error(request, _("Login yoki parol noto'g'ri!"))
    #             context.update(redirect=True)
    #             return render(request, 'account/login.html', context)
    #     except ObjectDoesNotExist:
    #         response = redirect(reverse_lazy('user:signup'))
    #         response.set_cookie('phone', phone, max_age=PHONE_MAX_AGE)
    #         return response
    # else:
    #     return render(request, 'account/login.html')


def handler404(request, exception):
    return render(request, '_parts/404.html', status=404)

def handler403(request, exception):
    return render(request, '_parts/403.html', status=403)



@login_required
def organizations_list(request):
    organizations = Organization.objects.filter(created_user=request.user, is_active=True).order_by('-id')
    if not organizations.exists():
        return redirect(reverse_lazy('user:add_organization'))
    context = {
        'organizations': organizations,
        'organization': organizations[0],
    }
    return render(request, 'user/organizations_list.html', context)


@login_required
def add_organization(request):
    regions = Region.objects.all()
    districts = District.objects.all()
    context = {
        'regions': regions,
        'districts': districts,
    }

    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    if request.is_ajax():
        if request.method == 'POST':
            organization = Organization.objects.create(title=request.POST.get('title', None))
            organization.director = request.POST.get('director', None)
            organization.identification_number = request.POST.get('identification_number', None)
            organization.address_of_garage = request.POST.get('address_of_garage', None)
            organization.legal_address_region = get_object_or_404(Region, id=request.POST.get('legal_address_region'))
            organization.legal_address_district = get_object_or_404(District,
                                                                    id=request.POST.get('legal_address_district'))
            # if request.FILES.get('license_photo'):
            #     organization.license_photo = request.FILES.get('license_photo', None)
            # if request.FILES.get('certificate_photo'):
            #     organization.certificate_photo = request.FILES.get('certificate_photo', None)
            organization.created_user = request.user
            organization.created_date = timezone.now()
            organization.save()

            company = serializers.serialize('json', [organization, ])
            struct = json.loads(company, )
            data = json.dumps(struct[0])
            return HttpResponse(data, content_type='json')
        else:
            return HttpResponse(False)

    return render(request, 'user/add_organization.html', context, )


@login_required
def edit_organization(request, organization_id):
    organization = get_object_or_404(Organization, id=organization_id)
    form = EditOrganizationForm(instance=organization)
    created_user = get_object_or_404(User, id=request.user.id)
    regions = Region.objects.all()
    if organization.created_user != created_user or organization.is_active == False:
        return render(request, '_parts/404.html')

    context = {
        'organization': organization,
        'form': form,
        'regions': regions
    }
    if request.POST:
        form = EditOrganizationForm(request.POST, instance=organization, )
        if form.is_valid():
            form = form.save(commit=False)
            if request.FILES:
                certificate_photo = request.FILES.get('certificate_photo')
                license_photo = request.FILES.get('license_photo')
                if certificate_photo:
                    form.license_photo = license_photo
                if license_photo:
                    form.certificate_photo = certificate_photo
                form.save()
            form.updated_date = timezone.now()
            form.save()
            messages.success(request, _("Muvaffaqiyatli tahrirlandi!"))
            return redirect(reverse_lazy('user:edit_organization', kwargs={'organization_id': organization.id}))
        else:
            messages.error(request, 'Formani to\'ldrishda xatolik1')

    return render(request, 'user/edit_organization.html', context)


@permission_classes([IsAuthenticated])
class Remove_Organization(APIView):
    def post(self, request):
        print(request.POST)
        if request.is_ajax():
            try:
                organization = get_object_or_404(Organization, id=request.POST.get('organization'))
                created_user = get_object_or_404(User, id=request.user.id)
                if organization.created_user != created_user:
                    return HttpResponse(False)
                organization.is_active = False
                organization.removed_date = timezone.now()
                organization.save()
                return HttpResponse(True)
            except:
                return HttpResponse(False)
        return redirect(reverse_lazy('user:organizations_list'))


def get_district(request):
    try:
        if request.is_ajax():
            districts = District.objects.filter(region=request.GET.get('region'))
            options = "<option value=''>--- --- ---</option>"

            for district in districts:

                options += f"<option value='{district.id}'>{district.title}</option>"
            return HttpResponse(options,status=200)
        else:
            return HttpResponse(status=404)
    except:
        return HttpResponse(status=404)


def get_quarters(request):
    if request.is_ajax():
        quarters = Quarter.objects.filter(district=request.GET.get('district'))
        options = "<option value=''>--- --- ---</option>"
        # options = ""
        for quarter in quarters:
            options += f"<option value='{quarter.id}'>{quarter.title}</option>"
        return HttpResponse(options)
    else:
        return False

class GetChildSections(AllowedRolesMixin):
    model = Section
    allowed_roles = [USER, DISTRICAL_CONTROLLER, REGIONAL_CONTROLLER, STATE_CONTROLLER, MODERATOR, ADMINISTRATOR, SUPER_ADMINISTRATOR]

    def get(self, request, *args, **kwargs):
        try:
            options = ""
            for item in self.get_queryset():
                options += f"<option value='{item.id}'>{item.title}</option>"
            return HttpResponse(options, status=200)
        except:
            return HttpResponse(False, status=404)

    def get_queryset(self, *args, **kwargs):
        try:
            qs = self.model.objects.filter(parent=self.request.GET.get('parent_section'))
            return qs
        except:
            return qs

@permission_classes([IsAuthenticated])
class Get_Organization(APIView):
    def post(self, request):
        if request.is_ajax():
            try:
                organization = get_object_or_404(Organization, id=request.POST.get('organization', None))
                company = serializers.serialize('json', [organization, ])
                struct = json.loads(company, )
                # data = json.dumps(struct[0])
                context = {
                    'organization': struct[0],
                    'legal_address_district': organization.legal_address_district.title,
                    'legal_address_region': organization.legal_address_region.title,
                    'created_date': datetime.datetime.strftime(organization.created_date, '%d.%m.%Y')
                }
                data = json.dumps(context)

                return HttpResponse(data, content_type='json', status=200)
            except:
                return HttpResponse(status=404)
        return HttpResponse(status=404)


@login_required
def edit_personal_data(request):

    form = EditForm(instance=request.user)
    regions = Region.objects.all()

    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    context = {
        'form': form,
        'regions': regions
    }
    if request.method == 'POST':
        try:
            token = request.COOKIES.get('token')
            Token.objects.get(key=token)
        except ObjectDoesNotExist:
            return HttpResponse(False)

        form = EditForm(request.POST, instance=request.user)
        if form.is_bound:
            if form.is_valid():
                form = form.save(commit=False)
                form.phone = request.POST.get('phone')
                form.username = request.POST.get('phone')
                form.turbo = request.POST.get('password')
                form.save()

                user = get_object_or_404(User, id=request.user.id)
                if user:
                    user.username = request.POST.get('phone')
                    user.turbo = request.POST.get('password')
                    user.set_password(request.POST.get('password'))
                    user.save()

                    user = authenticate(request, username=user.username, password=user.turbo)
                    if user is not None:
                        login(request, user)
                return HttpResponse(True)
            else:
                return HttpResponse(False)
        else:
            return HttpResponse(False)

    return render(request, 'user/edit_personal_data.html', context)




def get_code(request):
    if request.is_ajax():
        phone = request.GET.get('phone')
        try:
            user = User.objects.get(phone=phone)
            password = user.turbo
        except ObjectDoesNotExist:
            password = random.randint(10000, 99999)
            user = User.objects.create(username=phone, phone=phone, password=password, turbo=password)
            user.set_password(str(password))
            user.save()

        print(password)
        msg = f"E-RIB dasturidan ro'yhatdan o'tishni yakunlash va tizimga kirish ma'lumotlari  %0aLogin: {user.username} %0aParol: {user.turbo}"


        token, created = Token.objects.get_or_create(user=user)

        context = {
            'password': password
        }
        data = json.dumps(context)
        response = HttpResponse(data, content_type='json')
        response.set_cookie('token', token.key, max_age=TOKEN_MAX_AGE)
        return response
    else:
        return HttpResponse(False)


def get_user_pass(request):
    if request.is_ajax():
        phone = request.GET['phone']
        password = request.GET['password']
        try:
            User.objects.get(username=phone, turbo=password)
            return HttpResponse(True)
        except ObjectDoesNotExist:
            return HttpResponse(False)


def forgot_pass(request):
    if request.is_ajax():
        phone = int(request.GET['phone'])
        try:
            user_pass = User.objects.get(phone=phone)
            user = User.objects.get(phone=phone)
            msg = f"E-RIB dasturi login va parolingiz:%0aLogin: {user.username} %0aParol: {user.turbo}"
            msg = msg.replace(" ", "+")
            url = f"https://developer.apix.uz/index.php?app=ws&u={SMS_LOGIN}&h={SMS_TOKEN}&op=pv&to=998{phone}&msg={msg}"
            response = requests.get(url)
            return HttpResponse(True)
        except:
            return HttpResponse(False)


def get_phone(request):
    if request.is_ajax():
        phone = request.GET['phone']
        user = User.objects.filter(phone=phone)
        if user:
            return HttpResponse(True)


def is_register(request):
    if request.is_ajax():
        phone = request.GET.get('phone')
        try:
            user = User.objects.get(username=phone)
            if not user.is_staff and user.person_id == None:
                response = HttpResponse(False)
                response.set_cookie('phone', phone, max_age=PHONE_MAX_AGE)
                return response
            response = HttpResponse(True)
            response.set_cookie('phone', phone, max_age=PHONE_MAX_AGE)
            return response
        except ObjectDoesNotExist:
            response = HttpResponse(False)
            response.set_cookie('phone', phone, max_age=PHONE_MAX_AGE)
            return response


# def check_passport(request):
#     if request.is_ajax():
#         passport = request.GET['passport']
#         l = len(passport)
#         integ = ''
#         letters = ''
#         i = 0
#         while i < l:
#             passport_int = ''
#             a = passport[i]
#             while '0' <= a <= '9':
#                 passport_int += a
#                 i += 1
#                 if i < l:
#                     a = passport[i]
#                 else:
#                     break
#             else:
#                 if a != '':
#                     letters += a
#
#             i += 1
#             if passport_int != '':
#                 integ += passport_int
#
#         users1 = User.objects.filter(passport_number=int(integ))
#         users2 = User.objects.filter(passport_seriya=letters)
#         for user1 in users1:
#             for user2 in users2:
#                 if user1 == user2:
#                     return HttpResponse(True)
#         else:
#             return HttpResponse(False)
#     else:
#         return False


# def check_passport_with_number(request):
#     print('good')
#     if request.is_ajax():
#         passport_seriya = request.GET.get('passport_seriya', '')
#         passport_number = request.GET.get('passport_number', '')
#         print(f'{request.user.passport_seriya}, {type(request.user.passport_seriya)}')
#         print(f'{request.user.passport_number}, {type(request.user.passport_number)}')
#         print(f'{passport_seriya}, {type(passport_seriya)}')
#         print(f'{passport_number}, {type(passport_number)}')
#         if int(passport_number) == request.user.passport_number and passport_seriya == request.user.passport_seriya:
#             print('ok')
#             return HttpResponse(False)
#         print('end')
#         users1 = User.objects.filter(passport_number=passport_number)
#         users2 = User.objects.filter(passport_seriya=passport_seriya)
#
#         for user1 in users1:
#             for user2 in users2:
#                 if user1 == user2:
#                     return HttpResponse(True)
#
#         else:
#             return HttpResponse(False)
#     else:
#         return HttpResponse(False)

@permission_classes([IsAuthenticated])
class Save_User_Information(APIView):
    def post(self, request):
        if request.is_ajax():
            last_name = request.POST.get('last_name')
            first_name = request.POST.get('first_name')
            middle_name = request.POST.get('middle_name')
            birthday = datetime.datetime.strptime(request.POST.get('birthday'), '%Y-%m-%d')
            region = request.POST.get('region')
            district = request.POST.get('district')
            quarter = request.POST.get('quarter')
            address = request.POST.get('address')
            phone = request.POST.get('phone')
            user = User.objects.get(phone=phone)
            if user is not None:
                user.last_name = last_name
                user.first_name = first_name
                user.middle_name = middle_name
                user.birthday = birthday
                user.region_id = region
                user.district_id = district
                user.quarter_id = quarter
                user.address = address
                user.save()

                return HttpResponse(status=200)
            else:
                return HttpResponse(status=400)
        else:
            return HttpResponse(status=400)


@permission_classes([IsAuthenticated])
class save_passport_data(APIView):
    def post(self, request):
        if request.is_ajax():
            user = get_object_or_404(User, id=request.user.id)
            user = authenticate(request, username=user.phone, password=user.turbo)
            if user is not None:
                user.passport_seriya = request.POST.get('passport_seriya')
                user.passport_number = request.POST.get('passport_number')
                user.issue_by_whom = request.POST.get('issue_by_whom')
                user.person_id = request.POST.get('person_id')
                user.save()

                login(request, user)
                return HttpResponse(status=200)
            else:
                return HttpResponse(status=400)
        else:
            return HttpResponse(status=400)


class HelloView(View):
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get(self, request):
        print(request.user)
        return HttpResponse('GET')

    def post(self, request):
        print(request.user)
        return HttpResponse('POST')


class CustomAuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)

        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })


@permission_classes([IsAuthenticated])
class Get_Car_Type(APIView):
    def post(self, request):
        if request.is_ajax():
            try:
                car_id = request.POST.get('car')
                car = CarModel.objects.get(id=car_id)

                if car.is_truck:
                    is_truck = True
                else:
                    is_truck = False
                return HttpResponse(is_truck, status=200)
            except:
                return HttpResponse(status=400)
        else:
            return HttpResponse(status=400)


@login_required
def add_worker(request):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    context = {}
    if request.user.role == '7':
        sections = Section.objects.filter(parent__isnull=True, is_active=True)
        context.update(sections=sections)
        template = 'user/role/state_controller/add_worker.html'
    else:
        template =  'user/role/regional_controller/add_worker.html'

    if request.method == "POST":
        if request.user.role == STATE_CONTROLLER:
            section = request.POST.get('section')
            phone = request.POST.get('phone').replace('(', '').replace(')', '').replace('-', '').replace(' ', '')

            form = AddUserForm(data=request.POST)
            password = random.randint(1000000, 9999999)

            if form.is_valid():
                last_name = get_name(form.cleaned_data['last_name'])
                first_name = get_name(form.cleaned_data['first_name'])
                middle_name = get_name(form.cleaned_data['middle_name'])
                section = get_object_or_404(Section, id=section)
                region = get_object_or_404(Region, id=section.region.id)

                try:
                    user = User.objects.create_user(
                        username=phone,
                        turbo=password,
                        password=password,
                        last_name=last_name,
                        first_name=first_name,
                        middle_name=middle_name,
                        section=section,
                        region=region,
                        phone=phone,
                        role=REGIONAL_CONTROLLER,
                        is_superuser=False,
                        is_staff=True,
                    )
                    user.set_password(password)
                    user.username = phone
                    user.email = ''
                    user.save()

                    # msg = __("Hurmatli ") + str(user.last_name) + ' ' + str(user.first_name) + '!' + __("Sizning shaxsiy login va parolingiz.") + '%0a' + __('Login:') + str(user.username) + '%0a' + __("Parol:")  + str(user.turbo)
                    # print(msg)
                    # msg = msg.replace(" ", "+")
                    # url = f"https://developer.apix.uz/index.php?app=ws&u={SMS_LOGIN}&h={SMS_TOKEN}&op=pv&to=998{user.phone}&unicode=1&msg={msg}"
                    # response = requests.get(url)

                    messages.success(request, _('Xodim muvaffaqiyatli qo\'shildi!'))
                except IntegrityError:
                    messages.error(request, _("Bu raqam oldin ro'yhatdan o'tkazilgan !"))
        else:
            role = request.POST.get('worker')
            phone = request.POST.get('phone').replace('(', '').replace(')', '').replace('-', '').replace(' ', '')

            form = AddUserForm(data=request.POST)
            password = random.randint(1000000, 9999999)

            if form.is_valid():
                last_name = get_name(form.cleaned_data['last_name'])
                first_name = get_name(form.cleaned_data['first_name'])
                middle_name = get_name(form.cleaned_data['middle_name'])
                section = get_object_or_404(Section, id=request.user.section.id)

                if role == 'technical':
                    role = 5
                elif role == 'checker':
                    role = 3
                elif role == 'reviewer':
                    role = 4

                try:
                    user = User.objects.create_user(
                        username=phone,
                        turbo=password,
                        password=password,
                        last_name=last_name,
                        first_name=first_name,
                        middle_name=middle_name,
                        section=section,
                        phone=phone,
                        role=str(role),
                        is_superuser=False,
                        is_staff=True,
                    )
                    user.set_password(password)
                    user.username = phone
                    user.email = ''
                    user.save()

                    msg = f"Hurmatli {user.last_name} {user.first_name}! Sizning shaxsiy login va parolingiz. %0aLogin: {user.username}%0aParol: {user.turbo}"
                    msg = msg.replace(" ", "+")
                    url = f"https://developer.apix.uz/index.php?app=ws&u={SMS_LOGIN}&h={SMS_TOKEN}&op=pv&to=998{user.phone}&unicode=1&msg={msg}"
                    response = requests.get(url)

                    messages.success(request, 'Xodim muvaffaqiyatli qo\'shildi!')
                except IntegrityError:
                    messages.error(request, "Bu raqam oldin ro'yhatdan o'tkazilgan !")
    return render(request, template,context)


@login_required
def workers_list(request):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))
    if request.user.role == '7':
        workers = User.objects.filter(Q(role=6) & Q(is_active=True))
    else:
        workers = User.objects.filter(
            Q(Q(role=3) | Q(role=4) | Q(role=5)) & Q(is_active=True) & Q(section=request.user.section))
    if not workers.exists():
        messages.error(request, 'Xodimlar mavjud emas!')
    context = {
        'workers': workers
    }
    return render(request, 'user/role/state_controller/workers_list.html', context)


@login_required
def worker_delete(request, worker_id):
    worker = get_object_or_404(User, id=worker_id)
    if request.user.role == '2' and request.user.section == worker.section:
        worker.delete()
    else:
        return render(request, '_parts/404.html')


@login_required
def worker_edit(request, worker_id):
    worker = get_object_or_404(User, id=worker_id)
    if request.user.role == STATE_CONTROLLER:
        sections = Section.objects.filter(is_active=True, parent__isnull=True)
        regions = Region.objects.all()
        form = EditWorkerForm(instance=worker)
        context = {
            'form': form,
            'worker': worker,
            'regions': regions,
            'sections': sections,
        }

        if request.method == 'POST':
            try:
                phone = request.POST.get('phone').replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
                form = EditWorkerForm(request.POST, instance=worker)
                print(request.POST)
                section = get_object_or_404(Section, id=request.POST.get('section'))

                print(section)

                print(form.errors)
                if form.is_valid():
                    password = form.cleaned_data['password']
                    form = form.save(commit=False)
                    worker.set_password(password)

                    form.section = section
                    form.username = phone
                    form.phone = phone
                    form.turbo = password
                    form.save()
                    form = EditWorkerForm(instance=worker)

                    # msg = __("Hurmatli ") + str(worker.last_name) + ' ' + str(worker.first_name) + '!' + __("Sizning ma'lumotlaringiz tahrirlandi.") + '%0a' + __('Login:') + str(worker.username) + '%0a' + __("Parol:")  + str(worker.turbo)
                    # msg = msg.replace(" ", "+")
                    # url = f"https://developer.apix.uz/index.php?app=ws&u={SMS_LOGIN}&h={SMS_TOKEN}&op=pv&to=998{worker.phone}&unicode=1&msg={msg}"
                    # response = requests.get(url)
                    context.update(form=form)
                    messages.success(request, 'Muvaffaqiyatli tahrirlandi !')
                    return render(request, 'user/role/state_controller/edit_worker.html', context)
                else:
                    messages.error(request, "Formani to'ldirishda xatolik !")
                    return render(request, 'user/role/state_controller/edit_worker.html', context)
            except:
                messages.error(request, "Formani to'ldirishda xatolik !")
                return render(request, 'user/role/state_controller/edit_worker.html', context)
        return render(request, 'user/role/state_controller/edit_worker.html', context)
    elif request.user.role == REGIONAL_CONTROLLER:
        regions = Region.objects.all()
        form = EditWorkerForm(instance=worker)
        context = {
            'form': form,
            'worker': worker,
            'regions': regions,
        }

        if request.method == 'POST':
            try:
                phone = request.POST.get('phone').replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
                form = EditWorkerForm(request.POST, instance=worker)
                if form.is_valid():
                    password = form.cleaned_data['password']
                    form = form.save(commit=False)
                    worker.set_password(password)
                    form.phone = phone
                    form.turbo = password
                    form.save()
                    form = EditWorkerForm(instance=worker)

                    msg = f"Hurmatli {worker.last_name} {worker.first_name}! Sizning ma'lumotlaringiz tahrirlandi. %0aLogin: {worker.username}%0aParol: {worker.turbo}"
                    msg = msg.replace(" ", "+")
                    url = f"https://developer.apix.uz/index.php?app=ws&u={SMS_LOGIN}&h={SMS_TOKEN}&op=pv&to=998{worker.phone}&unicode=1&msg={msg}"
                    response = requests.get(url)
                    context.update(form=form)
                    messages.success(request, 'Muvaffaqiyatli tahrirlandi !')
                    return render(request, 'user/role/regional_controller/edit_worker.html', context)
                else:
                    messages.error(request, "Formani to'ldirishda xatolik !")
                    return render(request, 'user/role/regional_controller/edit_worker.html', context)
            except:
                messages.error(request, "Formani to'ldirishda xatolik !")
                return render(request, 'user/role/regional_controller/edit_worker.html', context)
        return render(request, 'user/role/regional_controller/edit_worker.html', context)
    else:
        return render(request, '_parts/404.html')


@login_required
def view_car_data(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    context = {

        'car': car
    }
    return render(request, 'user/car/view_car_data.html', context)


@login_required
def edit_car_data(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    form = EditCarForm(instance=car)

    models = CarModel.objects.filter(is_active=True)
    fuel_types = FuelType.objects.filter(is_active=True)
    car_types = CarType.objects.filter(is_active=True)
    devices = Device.objects.filter(is_active=True)
    bodyTypes = BodyType.objects.filter(is_active=True)
    colors = Color.objects.filter(is_active=True)
    histories = Car.objects.all()

    context = {
        'models': models,
        'fuel_types': fuel_types,
        'car_types': car_types,
        'devices': devices,
        'bodyTypes': bodyTypes,
        'color': colors,

        'form': form,
        'car': car,

        'histories': histories
    }

    if request.method == 'POST':
        try:
            form = EditCarForm(request.POST, instance=car)
            if request.POST.get('history'):
                history = get_object_or_404(Car, id=request.POST.get('history'))
            else:
                history = None

            devices = []
            if request.POST.getlist('devices'):
                for device_id in list(filter(None, request.POST.getlist('devices'))):
                    devices.append(get_object_or_404(Device, id=device_id))

            fuel_types = []
            if request.POST.getlist('fuel_types'):
                for fuel_type_id in list(filter(None, request.POST.getlist('fuel_types'))):
                    fuel_types.append(get_object_or_404(FuelType, id=fuel_type_id))


            if form.is_valid():
                given_number = request.POST.get('auction_number')

                form = form.save(commit=False)
                form.fuel_type.clear()
                form.device.clear()
                for fuel_type in fuel_types:
                    form.fuel_type.add(fuel_type)
                for device in devices:
                    form.device.add(device)
                form.given_number = given_number
                form.history = history
                form.save()
                return HttpResponse(True)
            else:
                return HttpResponse(False)
        except:
            return HttpResponse(False)

    return render(request, 'user/car/edit_car_data.html', context)

@login_required
def view_organization_data(request, id):
    organization = get_object_or_404(Organization, id=id)
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    context = {
        'organization': organization
    }
    return render(request, 'user/organization/view_organization_data.html', context)


@login_required
def view_personal_data(request, id):
    user = get_object_or_404(User, id=id)
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    context = {
        'user': user
    }
    return render(request, 'user/view_personal_data.html', context)


@login_required
def confirm_car_data(request, car_id):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    if request.user.role == '4' or request.user.role == '5':
        car = get_object_or_404(Car, id=car_id)
        application = get_object_or_404(Application, id=car.service_car.last().application_service.last().id)

        if application.process == '3':
            messages.error(request, f'{application.id}-raqamli ariza {application.process_sms} sababli rad etilgan!')
            return redirect(reverse_lazy('application:applications_list'))

        if request.method == 'GET':
            if request.GET.get('confirm') == 'True':
                if request.user.role == '4':
                    car.is_confirm = True
                    car.confirm_date = timezone.now()

                    messages.success(request, f"{car.model} {car.old_number if car.old_number else ''} transport vositasining dvigateli, shassi, kuzovi raqam belgilari muvaffaqiyatli tasdiqlandi!")

                    msg = f"Hurmatli foydalanuvchi! {application.id}-raqamli arizada ko'rsatilgan {car.model} {car.old_number if car.old_number else ''} transport vositasining dvigateli, shassi, kuzovi raqam belgilari muvaffaqiyatli tasdiqlandi! {'Transport vositangizni texnik ko*rikdan o*tkazib,' if not car.is_technical_confirm else ''} {'To*lovlarni kerakli hisob raqamlarga o*tkazib,' if not application.is_payment else ''} Hujjatlarning asl nusxalarini {request.user.section.title}ga olib kelishingizni so*raymiz!"
                    msg = msg.replace(" ", "+").replace('*', "'")
                    url = f"https://developer.apix.uz/index.php?app=ws&u={SMS_LOGIN}&h={SMS_TOKEN}&op=pv&to=998{application.created_user.phone}&msg={msg}"
                    response = requests.get(url)

                elif request.user.role == '5':
                    car.is_technical_confirm = True
                    car.technical_confirm = timezone.now()

                    messages.success(request,
                                     f"{car.model} {car.old_number if car.old_number else ''} transport vositasi texnik ko'rikdan muvaffaqiyatli o'tkazildi!")

                    msg = f"Hurmatli foydalanuvchi! {application.id}-raqamli arizada ko'rsatilgan {car.model} {car.old_number if car.old_number else ''} transport vositasi texnik ko'rikdan muvaffaqiyatli o'tkazildi! {'Transport vositangizni dvigateli, shassi, kuzovi raqam belgilari arizada ko*rsatilgandek ekanligini tasdiqlatib,' if not car.is_confirm else ''} {'To*lovlarni kerakli hisob raqamlarga o*tkazib,' if not application.is_payment else ''} Hujjatlarning asl nusxalarini {request.user.section.title}ga olib kelishingizni so*raymiz!"
                    msg = msg.replace(" ", "+").replace('*', "'")
                    url = f"https://developer.apix.uz/index.php?app=ws&u={SMS_LOGIN}&h={SMS_TOKEN}&op=pv&to=998{application.created_user.phone}&msg={msg}"
                    response = requests.get(url)
                car.save()
            elif request.GET.get('confirm') == 'False':
                if request.user.role == '4':
                    car.is_confirm = False
                    car.confirm_date = timezone.now()

                    messages.success(request,
                                     f"{car.model} {car.old_number if car.old_number else ''} transport vositasining dvigateli, shassi, kuzovi raqam belgilarining tasdiqlangani muvvaffaqiyatli bekor qilindi!")
                    msg = f"Hurmatli foydalanuvchi! {application.id}-raqamli arizada ko'rsatilgan {car.model} {car.old_number if car.old_number else ''} transport vositasining dvigateli, shassi, kuzovi raqam belgilari arizada ko*rsatilgan ma*lumotlar bilan mos emas!"
                    msg = msg.replace(" ", "+").replace('*', "'")
                    url = f"https://developer.apix.uz/index.php?app=ws&u={SMS_LOGIN}&h={SMS_TOKEN}&op=pv&to=998{application.created_user.phone}&msg={msg}"
                    response = requests.get(url)

                elif request.user.role == '5':
                    car.is_technical_confirm = False
                    car.technical_confirm = timezone.now()

                    messages.success(request,
                                     f"{car.model} {car.old_number if car.old_number else ''} transport vositasi texnik nosoz ekanligi muvaffaqiyatli tasdiqlandi!")

                    msg = f"Hurmatli foydalanuvchi! {application.id}-raqamli arizada ko'rsatilgan {car.model} {car.old_number if car.old_number else ''} transport vositasi texnik nosoz deb topildi!"
                    msg = msg.replace(" ", "+").replace('*', "'")
                    url = f"https://developer.apix.uz/index.php?app=ws&u={SMS_LOGIN}&h={SMS_TOKEN}&op=pv&to=998{application.created_user.phone}&msg={msg}"
                    response = requests.get(url)
                car.save()

            return redirect(reverse_lazy('application:applications_list'))
        else:
            return redirect(reverse_lazy('application:applications_list'))
    else:
        return render(request, '_parts/404.html')


@permission_classes([IsAuthenticated])
class Save_New_Car_Model(APIView):
    def post(self, request):
        if request.is_ajax():
            if request.POST.get('is_local') == 'true':
                is_local = True
            else:
                is_local = False

            if request.POST.get('is_truck') == 'true':
                is_truck = True
            else:
                is_truck = False

            try:
                model = CarModel.objects.filter(title__iexact=request.POST.get('title'),is_truck=is_truck, is_local=is_local)
                if model.exists():
                    return HttpResponse(status=409)
                CarModel.objects.create(title=request.POST.get('title'), is_truck=is_truck, is_local=is_local,created_user=request.user)
                car_models = CarModel.objects.filter(is_active=True)
                options = ""
                for car_model in car_models:
                    options += f"<option value='{car_model.id}'>{car_model.title}</option>"
                return HttpResponse(options, status=200)
            except:
                return HttpResponse(status=400)
        else:
            return HttpResponse(status=400)


@permission_classes([IsAuthenticated])
class Save_New_Color(APIView):
    def post(self, request):
        if request.is_ajax():
            try:
                color = Color.objects.filter(title__iexact=request.POST.get('color'))
                if color.exists():
                    return HttpResponse(status=409)
                Color.objects.create(title=request.POST.get('color'), created_user=request.user)
                colors = Color.objects.filter(is_active=True)
                options = ""
                for color in colors:
                    options += f"<option value='{color.id}'>{color.title}</option>"
                return HttpResponse(options, status=200)
            except:
                return HttpResponse(status=400)
        else:
            return HttpResponse(status=400)

@login_required
def getDistricts(request):
    id = request.GET.get('id',None)
    if id:
        result = list(District.objects.filter(region_id=int(id)).values('id', 'title'))
        return HttpResponse(json.dumps(result), content_type="application/json")





@login_required
def regions_list(request):
    if request.user.role == '7':
        regions_list = Section.objects.filter(parent__isnull=True)
        context = {
            'regions_list': regions_list
        }
        return render(request, 'user/role/state_controller/regions_list.html', context)
    else:
        return render(request, '_parts/404.html')

@login_required
def sections_list(request, section_id):
    if request.user.role == '6' or request.user.role == '7':
        parent_section = get_object_or_404(Section, id=section_id)
        sections = Section.objects.filter(parent=parent_section)

        context = {
            'parent_section': parent_section,
            'sections': sections,

        }
        return render(request, 'user/role/regional_controller/sections_list.html', context)
    else:
        return render(request, '_parts/404.html')


class SectionsListByRegion(AllowedRolesMixin, View):
    allowed_roles = [USER, DISTRICAL_CONTROLLER, REGIONAL_CONTROLLER, STATE_CONTROLLER, MODERATOR, ADMINISTRATOR, SUPER_ADMINISTRATOR]
    def get(self, request, *args, **kwargs):
        if request.GET.get('region', None):
            qs = Section.objects.filter(region=request.GET.get('region'), parent__isnull=False)
            sections = serializers.serialize('json', qs)
            return HttpResponse(sections, status=200,content_type='application/json')
        return HttpResponse(status=404)

