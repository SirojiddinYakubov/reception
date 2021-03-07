import json
import random
import uuid

from allauth.account.views import login
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from djoser.serializers import UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes, api_view
from rest_framework.fields import CurrentUserDefault
from rest_framework.permissions import *
from rest_framework.views import APIView

from application.models import *
from reception.settings import BASE_DIR
from user.utils import render_to_pdf
from .forms import *
from .models import *
from user.models import *
from docxtpl import DocxTemplate


# Create your views here.

@login_required
def account_statement_insert(request):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

    # get previous years
    year = datetime.datetime.today().year
    years = range(year, year - 80, -1)
    cars = CarModel.objects.all()
    devices = Devices.objects.filter(is_active=True)
    bodyTypes = BodyType.objects.filter(is_active=True)
    colors = Color.objects.filter(is_active=True)
    organizations = Organization.objects.filter(created_user=request.user, is_active=True)

    context = {
        'cars': cars,
        'organizations': organizations,
        'devices': devices,
        'bodyTypes': bodyTypes,
        'years': years,
        'color': colors
    }
    return render(request, 'account_statement/account_statement_insert.html', context=context)


@login_required
def add_photo(request, id):
    data = AccountStatement.objects.get(id=id)
    context = {
        'data': data
    }
    return render(request, 'account_statement/add-photo.html', context=context)


@permission_classes([IsAuthenticated])
class Save_Account_Statement_And_Car(APIView):
    def post(self, request):
        if request.is_ajax():
            person_type = request.POST.get('person_type')
            engine_number = request.POST.get('engine_number')
            body_number = request.POST.get('body_number')
            color = get_object_or_404(Color, id=request.POST.get('color', None))
            made_year = request.POST.get('made_year')
            devices = []
            post_devices = list(request.POST.get('devices', None).replace(',', ''))
            if request.POST.get('devices'):
                for device_id in post_devices:
                    devices.append(get_object_or_404(Devices, id=device_id))
            seriya = request.POST.get('account_statement')
            date_conclusion_contract = datetime.datetime.strptime(request.POST.get('date_conclusion_contract', None),'%d.%m.%Y')
            user = get_object_or_404(User, id=request.user.id)
            get_car = get_object_or_404(CarModel, id=request.POST.get('car'))

            # create car
            car = Car.objects.create(model=get_car)
            if request.POST.get('body_type'):
                car.body_type = get_object_or_404(BodyType, id=request.POST.get('body_type', None))
            if request.POST.get('chassis_number', None):
                car.chassis_number = request.POST.get('chassis_number', None)
            car.body_number = body_number
            car.engine_number = engine_number
            car.made_year = made_year
            car.color = color
            for device in devices:
                car.devices.add(device)
            car.save()

            # create application and account_statament
            application = Application.objects.create(created_user=user, created_date=timezone.now())
            account_statement = AccountStatement.objects.create(person_type=person_type, car=car)
            account_statement.seriya = seriya
            account_statement.date_conclusion_contract = date_conclusion_contract
            account_statement.created_user = request.user
            if person_type == 'Y':
                organization = get_object_or_404(Organization, id=request.POST.get('organization'))
                application.person_type = person_type
                account_statement.organization = organization
            account_statement.save()
            service = Service.objects.create(account_statement=account_statement)
            application.service = service

            password = random.randint(1000, 9999)
            application.password = password
            application.save()

            app = serializers.serialize('json', [application, ])
            struct = json.loads(app)
            data = json.dumps(struct[0])
            return HttpResponse(data, content_type='json')
        else:
            return HttpResponse(False)


@login_required
def export_to_word(request, id):
    doc = DocxTemplate("static/online/account_statement_example.docx")
    user = User.objects.get(username=request.user.username)
    data = get_object_or_404(AccountStatement, id=id)
    now_date = datetime.date.today()
    context = {
        'user': user,
        'data': data,
        'now_date': now_date
    }
    doc.render(context)
    doc.save(f"media/document/account_statement/{data.id}.docx")
    return HttpResponse()
