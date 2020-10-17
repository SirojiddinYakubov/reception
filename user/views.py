import json
import random

import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.urls import reverse_lazy
from docxtpl import DocxTemplate
from xhtml2pdf import pisa

from user.decorators import *
from user.forms import *
import reportlab
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas

from user.utils import render_to_pdf

@login_required
def index(request):
    # generate pdf

    # html holatda ekranga chiqarish

    template = get_template('user/index.html')
    passport = '{} {}'.format(request.user.passport_seriya, request.user.passport_number)
    context = {
        'user': request.user,
        'passport': passport,
        'request': request
    }

    html = template.render(context)
    download = request.GET.get('download')
    if download:
        doc = DocxTemplate("static/online/user_information.docx")
        doc.render(context)
        doc.save(f"media/document/user/Shaxsiy ma'lumotnoma #{request.user.id}.docx")
    return HttpResponse(html)


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
    if not request.COOKIES.get('phone'):
        return redirect(reverse_lazy('user:login_first'))
    phone = request.COOKIES['phone']
    context = {
        'regions': regions,
        'phone': phone
    }
    try:
        user = User.objects.get(phone=phone)
        next1 = 'true'
        context.update(next1=next1)
        if user.last_name != '':
            next2 = 'true'
            context.update(next2=next2)
            return render(request, 'account/signup.html', context)
        if user.person_id != None:
            return redirect(reverse_lazy('user:login_first'))
        return render(request, 'account/signup.html', context)
    except ObjectDoesNotExist:
        return render(request, 'account/signup.html', context)

    # if request.POST:
    #     form = SignUpForm(request.POST or None)
    #     password = int(request.POST['confirm_password'])
    #     phone = int(request.POST['phone'])
    #     if not User.objects.get(phone=phone, password=password):
    #         messages.error(request, "Tasdiqlash kodi noto'g'ri")
    #     if form.is_valid():
    #         passport = request.POST['passport']
    #         document_issue = form.cleaned_data['document_issue']
    #         document_expiry = form.cleaned_data['document_expiry']
    #         issue_by_whom = form.cleaned_data['issue_by_whom']
    #         last_name = form.cleaned_data['last_name']
    #         first_name = form.cleaned_data['first_name']
    #         middle_name = form.cleaned_data['middle_name']
    #         region = get_object_or_404(Region, id=request.POST['region'])
    #         district = get_object_or_404(District, id=request.POST['district'])
    #         mfy = get_object_or_404(MFY, id=request.POST['mfy'])
    #         address = form.cleaned_data['address']
    #         birthday = request.POST['birthday']
    #         person_id = request.POST.get('person_id', '')
    #
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
    #         user = User.objects.create_user(
    #             username=phone,
    #             passport_seriya=letters,
    #             passport_number=int(integ),
    #             document_issue=document_issue,
    #             document_expiry=document_expiry,
    #             issue_by_whom=issue_by_whom,
    #             turbo=password,
    #             last_name=last_name,
    #             first_name=first_name,
    #             middle_name=middle_name,
    #             region=region,
    #             district=district,
    #             mfy=mfy,
    #             address=address,
    #             birthday=birthday,
    #             phone=phone,
    #             is_superuser=False,
    #             person_id=person_id,
    #         )
    #         user.set_password(password)
    #         user.username = passport
    #         user.email = ''
    #         user.save()
    #         user = authenticate(username=phone, password=password)
    #         if user is not None:
    #             if user.is_active:
    #                 login(request, user)
    #         return redirect(reverse_lazy('user:index'))
    #     else:
    #         messages.error(request, "Formani to'ldirishda xatolik !")
    # else:
    #     form = SignUpForm()
    # return render(request, 'account/signup.html', context)


@login_required
def user_logout(request):
    return render(request, 'account/logout.html')


def login_first(request):
    if request.method == 'POST':
        phone = request.POST.get('phone', None)
        password = request.POST.get('password', '')
        context = {
            'phone': phone
        }
        if len(str(phone)) != 9:
            phone = request.COOKIES['phone']
        try:
            user1 = User.objects.get(phone=phone)
            if user1.person_id == None:
                return redirect(reverse_lazy('user:signup'))
            user = authenticate(request, username=phone, password=password)
            if user is not None:
                login(request, user)
                return redirect(reverse('user:index'))
            else:
                messages.error(request, "Login yoki parol noto'g'ri!")
                context.update(redirect=True)
                return render(request, 'account/login.html', context)
        except ObjectDoesNotExist:
            response = redirect(reverse_lazy('user:signup'))
            response.set_cookie('phone', phone, max_age=300)
            return response
    else:
        return render(request, 'account/login.html')


@login_required
def view_organizations(request):
    organizations = Organization.objects.filter(created_user=request.user, is_active=True).order_by('-id')
    if not organizations:
        return render(request, 'user/add_organization.html')
    context = {
        'organizations': organizations,
        'organization': organizations[0],
    }
    return render(request, 'user/view_organizations.html', context)

@login_required
def add_organization(request):
    if request.is_ajax():
        if request.method == 'POST':
            organization = Organization.objects.create(title=request.POST.get('title', None))
            organization.director = request.POST.get('director', None)
            organization.identification_number = request.POST.get('identification_number', None)
            organization.legal_address = request.POST.get('legal_address', None)
            organization.address_of_garage = request.POST.get('address_of_garage', None)
            organization.license_photo = request.FILES.get('license_photo', None)
            organization.certificate_photo = request.FILES.get('certificate_photo', None)
            organization.created_user = request.user
            organization.created_date = timezone.now()
            organization.save()
            return HttpResponse(True)
        else:
            return HttpResponse(False)
    return render(request, 'user/add_organization.html',)

@login_required
def edit_organization(request, organization_id):
    organization = get_object_or_404(Organization, id=organization_id)
    created_user = get_object_or_404(User, id=request.user.id)
    context = {
        'organization': organization,

    }

    if organization.created_user != created_user:
        return redirect(reverse_lazy('user:view_organizations'))

    if request.is_ajax():
        if request.method == 'POST':
            organization.director = request.POST.get('director', None)
            organization.identification_number = request.POST.get('identification_number', None)
            organization.legal_address = request.POST.get('legal_address', None)
            organization.address_of_garage = request.POST.get('address_of_garage', None)
            organization.created_user = request.user
        if request.FILES:
            if request.FILES.get('license_photo'):
                organization.license_photo = request.FILES.get('license_photo', None)
            if request.FILES.get('certificate_photo'):
                organization.certificate_photo = request.FILES.get('certificate_photo', None)
        organization.updated_date = timezone.now()
        organization.save()
        return HttpResponse(True)
    return render(request, 'user/edit_organization.html', context)

@login_required
def remove_organization(request, organization_id):
    if request.is_ajax():
        if request.method == 'GET':
            created_user = get_object_or_404(User, id=request.user.id)
            organization = get_object_or_404(Organization, id=organization_id)
            if organization.created_user != created_user:
                return HttpResponse(False)
            organization.is_active = False
            organization.removed_date = timezone.now()
            organization.save()
            return HttpResponse(True)
        return HttpResponse(False)
    return redirect(reverse_lazy('user:view_organizations'))

# def login_second(request):
#     if request.method == 'POST':
#
#         username = request.POST['passport']
#         password = request.POST['password'].replace(' ', '')
#         user = authenticate(username=username, password=password)
#         if user is not None:
#             if user.is_active:
#                 # if request.POST['checkbox']:
#                 #     response = HttpResponse('cookie example')
#                 #     response.set_cookie('username', username)
#                 #     response.set_cookie('password', password)
#                 login(request, user)
#                 return redirect(reverse_lazy('user:index'))
#             else:
#                 messages.error(request, 'Sizning profilingiz aktiv holatda emas !')
#                 return render(request, 'account/login_second.html')
#         else:
#             messages.error(request, "Login yoki parol noto'g'ri!")
#             return render(request, 'account/login_second.html')
#     else:
#         return render(request, 'account/login_second.html')


def get_district(request):
    if request.is_ajax():
        districts = District.objects.filter(region=request.GET.get('region'))
        options = "<option>--- --- ---</option>"
        for district in districts:
            options += f"<option value='{district.id}'>{district.title}</option>"
        return HttpResponse(options)
    else:
        return False




@login_required
def get_organization(request):
    if request.is_ajax():
        if request.method == 'GET':
            organization = get_object_or_404(Organization, id=request.GET.get('organization', None))
            company = serializers.serialize('json', [organization, ])
            struct = json.loads(company)
            data = json.dumps(struct[0])
            return HttpResponse(data, content_type='json')
    return JsonResponse(False)

@login_required
def edit(request):
    form = EditForm(instance=request.user)
    context = {
        'form': form
    }
    if request.method == 'POST':
        if form.is_bound:
            if form.is_valid():
                form = form.save(commit=False)
                form.phone = request.POST.get('phone', '')
                form.save()
            else:
                messages.error(request, "Formani to'ldirishda xatolik!")
        else:
            messages.error(request, "Formani to'ldiring!")

    return render(request, 'user/edit.html', context)


def get_mfy(request):
    if request.is_ajax():
        mfys = MFY.objects.filter(district=request.GET.get('district'))
        options = "<option>--- --- ---</option>"
        for mfy in mfys:
            options += f"<option value='{mfy.id}'>{mfy.title}</option>"
        return HttpResponse(options)
    else:
        return False


def get_code(request):
    if request.is_ajax():
        # phone = request.GET.get('phone', False)
        # if 'phone' in request.session:
        #     if 'password' in request.session:
        #         password = request.session.get('password', False)
        #     else:
        #         password = random.randint(1000000, 9999999)
        #         request.session['password'] = password
        # else:
        #     password = random.randint(1000000, 9999999)
        #     request.session['password'] = password

        phone = request.GET.get('phone')
        try:
            user = User.objects.get(phone=phone)
            password = user.turbo
        except ObjectDoesNotExist:
            password = random.randint(10000, 99999)
            user = User.objects.create(username=phone, phone=phone, password=password, turbo=password)
            user.set_password(password)
            user.save()
        # msg = f"E-RIB dasturidan ro'yhatdan o'tishni yakunlash va tizimga kirish ma'lumotlari  %0aLogin: {request.GET.get('phone')} %0aParol: {password}"
        # msg = msg.replace(" ", "+")
        # url = f"https://developer.apix.uz/index.php?app=ws&u=jj39k&h=cb547db5ce188f49c1e1790c25ca6184&op=pv&to=998{request.GET.get('phone')}&msg={msg}"
        # response = requests.get(url)
        print(password)
        # for key, value in request.session.items():
        #     print(key, value)
        return HttpResponse(password)
    else:
        return False


def get_user_pass(request):
    if request.is_ajax():
        phone = request.GET['phone']
        password = request.GET['password']
        try:
            User.objects.get(phone=phone, password=password)
            return HttpResponse(True)
        except ObjectDoesNotExist:
            return HttpResponse(False)


def forgot_pass(request):
    if request.is_ajax():
        phone = int(request.GET['phone'])
        try:
            user_pass = User.objects.get(phone=phone)
            user = User.objects.get(phone=phone)
            msg = f"E-RIB dasturi passport va parolingiz:%0aPassport: {user.passport_seriya}{user.passport_number} %0aParol: {user.turbo}"
            msg = msg.replace(" ", "+")
            url = f"https://developer.apix.uz/index.php?app=ws&u=jj39k&h=cb547db5ce188f49c1e1790c25ca6184&op=pv&to=998{phone}&msg={msg}"
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
        user = User.objects.get(phone=phone)
        if user.person_id == None:
            response = HttpResponse(False)
            response.set_cookie('phone', phone, max_age=300)
            return response
        response = HttpResponse(True)
        response.set_cookie('phone', phone, max_age=300)
        return response
    except ObjectDoesNotExist:
        response = HttpResponse(False)
        response.set_cookie('phone', phone, max_age=300)
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


def save_user_information(request):
    if request.is_ajax():
        if request.GET:
            last_name = request.GET.get('last_name')
            first_name = request.GET.get('first_name')
            middle_name = request.GET.get('middle_name')
            birthday = request.GET.get('birthday')
            region = request.GET.get('region')
            district = request.GET.get('district')
            mfy = request.GET.get('mfy')
            address = request.GET.get('address')
            phone = request.GET.get('phone')
            user = User.objects.get(phone=phone)
            if user:
                user.last_name = last_name
                user.first_name = first_name
                user.middle_name = middle_name
                user.birthday = birthday
                user.region_id = region
                user.district_id = district
                user.mfy_id = mfy
                user.address = address
                user.save()
            else:
                return HttpResponse(False)
        return HttpResponse(True)


def upload_file(request):
    if request.is_ajax():
        file = request.FILES.get('file')
        phone = request.POST.get('phone')
        user = User.objects.get(phone=phone)
        user.passport_photo = file
        user.passport_seriya = request.POST.get('passport_seriya')
        user.passport_number = request.POST.get('passport_number')
        user.issue_by_whom = request.POST.get('issue_by_whom')
        user.document_issue = request.POST.get('document_issue')
        user.document_expiry = request.POST.get('document_expiry')
        user.person_id = request.POST.get('person_id')
        user.save()
        user = authenticate(request, username=phone, password=user.turbo)
        if user is not None:
            login(request, user)
            return HttpResponse(True)
        else:
            return HttpResponse(False)
    else:
        return HttpResponse(False)


