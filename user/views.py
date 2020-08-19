import random

import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

from django.http import HttpResponse
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


def index(request):
    # generate pdf

    # html holatda ekranga chiqarish

    template = get_template('user/index.html')
    passport = '{} {}'.format(request.user.passport_seriya, request.user.passport_number)
    context = {
        'user': request.user,
        'passport': passport
    }
    if request.user.gender == 'M':
        context.update(gender='Erkak')
    elif request.user.gender == 'W':
        context.update(gender='Ayol')
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
    nationalities = Nationality.objects.all()

    context = {
        'regions': regions,
        'nationalities': nationalities,
    }

    if request.POST:
        form = SignUpForm(request.POST or None)
        password = int(request.POST['confirm_password'])
        phone = int(request.POST['phone'])
        if not UserPassword.objects.get(phone=phone, password=password):
            messages.error(request, "Tasdiqlash kodi noto'g'ri")
        if form.is_valid():
            passport = request.POST['passport']
            document_issue = form.cleaned_data['document_issue']
            document_expiry = form.cleaned_data['document_expiry']
            issue_by_whom = form.cleaned_data['issue_by_whom']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            nationality = get_object_or_404(Nationality, id=request.POST['nationality'])
            region = get_object_or_404(Region, id=request.POST['region'])
            district = get_object_or_404(District, id=request.POST['district'])
            mfy = get_object_or_404(MFY, id=request.POST['mfy'])
            address = form.cleaned_data['address']
            birthday = request.POST['birthday']
            gender = form.cleaned_data['gender']

            l = len(passport)
            integ = ''
            letters = ''
            i = 0
            while i < l:
                passport_int = ''
                a = passport[i]
                while '0' <= a <= '9':
                    passport_int += a
                    i += 1
                    if i < l:
                        a = passport[i]
                    else:
                        break
                else:
                    if a != '':
                        letters += a

                i += 1
                if passport_int != '':
                    integ += passport_int

            user = User.objects.create_user(
                username=passport,
                passport_seriya=letters,
                passport_number=int(integ),
                document_issue=document_issue,
                document_expiry=document_expiry,
                issue_by_whom=issue_by_whom,
                turbo=password,
                last_name=last_name,
                first_name=first_name,
                middle_name=middle_name,
                nationality=nationality,
                region=region,
                district=district,
                mfy=mfy,
                address=address,
                birthday=birthday,
                gender=gender,
                phone=phone,
                is_superuser=False,
            )
            user.set_password(password)
            user.username = passport
            user.email = ''
            user.save()
            user = authenticate(username=passport, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
            return redirect(reverse_lazy('user:index'))
        else:
            messages.error(request, "Formani to'ldirishda xatolik !")
    else:
        form = SignUpForm()
    return render(request, 'account/signup.html', context)


@login_required
def user_logout(request):
    return render(request, 'account/logout.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST['passport']
        password = request.POST['password'].replace(' ', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                # if request.POST['checkbox']:
                #     response = HttpResponse('cookie example')
                #     response.set_cookie('username', username)
                #     response.set_cookie('password', password)
                login(request, user)
                return redirect(reverse_lazy('account_statement:index'))
            else:
                messages.error(request, 'Sizning profilingiz aktiv holatda emas !')
                return render(request, 'account/login.html')
        else:
            messages.error(request, "Login yoki parol noto'g'ri!")
            return render(request, 'account/login.html')
    else:
        return render(request, 'account/login.html')


def get_district(request):
    if request.is_ajax():
        districts = District.objects.filter(region=request.GET.get('region'))
        options = "<option>--- --- ---</option>"
        for district in districts:
            options += f"<option value='{district.id}'>{district.title}</option>"
        return HttpResponse(options)
    else:
        return False


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
        password = random.randint(1000000, 9999999)
        phone = request.GET.get('phone')
        try:
            if UserPassword.objects.get(phone=phone):
                user_pass = UserPassword.objects.get(phone=phone)
                user_pass.password = password
                user_pass.save()
        except ObjectDoesNotExist:
            UserPassword.objects.create(phone=phone, password=password)
        # msg = f"E-RIB dasturidan ro'yhatdan o'tishni yakunlash va tizimga kirish ma'lumotlari  %0aLogin: {request.GET.get('phone')} %0aParol: {password}"
        # msg = msg.replace(" ", "+")
        # url = f"https://developer.apix.uz/index.php?app=ws&u=jj39k&h=cb547db5ce188f49c1e1790c25ca6184&op=pv&to=998{request.GET.get('phone')}&msg={msg}"
        # response = requests.get(url)
        print(password)
        return HttpResponse(password)
    else:
        return False


def get_user_pass(request):
    if request.is_ajax():
        phone = request.GET['phone']
        password = request.GET['password']
        try:
            UserPassword.objects.get(phone=phone, password=password)
            return HttpResponse(True)
        except ObjectDoesNotExist:
            return HttpResponse(False)


def forgot_pass(request):
    if request.is_ajax():
        phone = int(request.GET['phone'])
        try:
            user_pass = UserPassword.objects.get(phone=phone)
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


def check_passport(request):
    if request.is_ajax():
        passport = request.GET['passport']
        l = len(passport)
        integ = ''
        letters = ''
        i = 0
        while i < l:
            passport_int = ''
            a = passport[i]
            while '0' <= a <= '9':
                passport_int += a
                i += 1
                if i < l:
                    a = passport[i]
                else:
                    break
            else:
                if a != '':
                    letters += a

            i += 1
            if passport_int != '':
                integ += passport_int

        users1 = User.objects.filter(passport_number=int(integ))
        users2 = User.objects.filter(passport_seriya=letters)
        for user1 in users1:
            for user2 in users2:
                if user1 == user2:
                    return HttpResponse(True)
        else:
            return HttpResponse(False)
    else:
        return False
