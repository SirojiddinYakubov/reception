import datetime
import io
import json
import random
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from docxtpl import DocxTemplate
from rest_framework.authtoken.models import Token
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from xhtml2pdf import pisa

from application.models import Application, Service
from contract_of_sale.models import ContractOfSale
from gift_agreement.models import GiftAgreement
from reception.settings import BASE_DIR
from user.models import *
# Create your views here.
@login_required
def contract_of_sale_index(request):
    try:
        token = request.COOKIES.get('token')
        Token.objects.get(key=token)
    except ObjectDoesNotExist:
        return redirect(reverse_lazy('user:custom_logout'))

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
    return render(request, 'service/contract_of_sale/contract_of_sale_insert.html', context)

@permission_classes([IsAuthenticated])
class Save_Contract_Of_Sale_And_Car(APIView):
    def post(self, request):
        if request.is_ajax():
            person_type = request.POST.get('person_type')
            engine_number = request.POST.get('engine_number')
            body_number = request.POST.get('body_number')
            color = get_object_or_404(Color, id=request.POST.get('color', None))

            if request.POST.get('lost_technical_passport') == 'on':
                lost_technical_passport = True
            else:
                lost_technical_passport = False

            made_year = request.POST.get('made_year')
            devices = []
            post_devices = list(request.POST.get('devices', None).replace(',', ''))
            if request.POST.get('devices'):
                for device_id in post_devices:
                    devices.append(get_object_or_404(Devices, id=device_id))
            seriya = request.POST.get('contract_of_sale')
            date_conclusion_contract = datetime.datetime.strptime(request.POST.get('date_conclusion_contract', None),
                                                                  '%d.%m.%Y')
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
            car.lost_technical_passport = lost_technical_passport
            for device in devices:
                car.devices.add(device)
            car.save()

            # create application and account_statament
            application = Application.objects.create(created_user=user, created_date=timezone.now())
            contract_of_sale = ContractOfSale.objects.create(person_type=person_type, car=car)
            contract_of_sale.seriya = seriya
            contract_of_sale.date_conclusion_contract = date_conclusion_contract
            contract_of_sale.created_user = request.user
            if person_type == 'Y':
                organization = get_object_or_404(Organization, id=request.POST.get('organization'))
                application.person_type = person_type
                contract_of_sale.organization = organization

            contract_of_sale.save()
            service = Service.objects.create(contract_of_sale=contract_of_sale)
            application.service = service

            application.password = random.randint(1000, 9999)
            application.save()


            app = serializers.serialize('json', [application, ])
            struct = json.loads(app)
            data = json.dumps(struct[0])
            return HttpResponse(data, content_type='json')
        else:
            return HttpResponse(False)