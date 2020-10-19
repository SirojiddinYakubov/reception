import datetime
import json
import os
import random

from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.utils import timezone
from docxtpl import DocxTemplate

from account_statement.models import AccountStatement
from application.models import Application
from user.models import User, Organization, Car
from user.utils import render_to_pdf


@login_required
def index(request):
    applications = Application.objects.all()
    context = {
        'applications': applications
    }
    return render(request, 'application/index.html', context)


@login_required
def detail(request, id):
    application = get_object_or_404(Application, id=id)
    context = {
        'application': application
    }
    return render(request, 'application/detail.html', context)


def admin_url_params_encoded(request):
    pass


@login_required
def application_pdf(request, id):
    application = get_object_or_404(Application, id=id)
    context = {
        'now_date': f'{datetime.date.today().day}.{datetime.date.today().month}.{datetime.date.today().year}',
        'created_date': f'{application.created_date.day}.{application.created_date.month}.{application.created_date.year}',
        'updated_date': f'{application.updated_date.day}.{application.updated_date.month}.{application.updated_date.year}',
        'app': application
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
def save_application_information(request):
    if request.is_ajax():
        # get request arg
        person_type = request.POST.get('person_type')
        engine_number = request.POST.get('engine_number')
        body_number = request.POST.get('body_number')
        color = request.POST.get('color')
        made_year = request.POST.get('made_year')
        additionality = request.POST.get('additionality')
        cert_seriya = request.POST.get('cert_seriya')
        cert_number = request.POST.get('cert_number')
        date_conclusion_contract = request.POST.get('date_conclusion_contract')
        accountStatementPhoto = request.FILES.get('accountStatementPhoto')
        user = get_object_or_404(User, id=request.user.id)
        get_car = get_object_or_404(Car, id=request.POST.get('car'))

        # create car
        car = Car.objects.create(model=get_car.model, is_local=get_car.is_local, is_truck=get_car.is_truck)
        if request.POST.get('body_type') and request.POST.get('chassis_number'):
            car.body_type = request.POST.get('body_type')
            car.chassis_number = request.POST.get('chassis_number')
        car.body_number = body_number
        car.engine_number = engine_number
        car.made_year = made_year
        car.color = color
        car.additionally = additionality
        car.save()

        # create application and account_statament
        application = Application.objects.create(created_user=user, created_date=timezone.now())
        account_statement = AccountStatement.objects.create(person_type=person_type, car=car)
        account_statement.cert_seriya = cert_seriya
        account_statement.cert_number = cert_number
        account_statement.date_conclusion_contract = date_conclusion_contract
        account_statement.cert_photo = accountStatementPhoto
        if person_type == 'Y':
            organization = get_object_or_404(Organization, id=request.POST.get('organization'))
            application.is_legal = True
            account_statement.organization = organization

        account_statement.save()

        application.account_statement = account_statement

        # application photo
        now_date = datetime.date.today()
        context = {
            'data': account_statement,
            'now_date': now_date,
            'car': car,
            'state': f"{account_statement.cert_seriya} № {account_statement.cert_number} {account_statement.date_conclusion_contract}",
            'user': request.user

        }

        if car.is_truck:
            context.update(type='Юк')
        else:
            context.update(type='Енгил')

        if car.is_local:
            context.update(local='Махаллий')
        else:
            context.update(local="Чет эл")

        if request.POST.get('organization'):
            organization = get_object_or_404(Organization, id=request.POST.get('organization'))
            context.update(org=organization)
            doc = DocxTemplate(f"static{os.sep}online{os.sep}account_statement{os.sep}account_statement_legal.docx")
        else:
            doc = DocxTemplate(f"static{os.sep}online{os.sep}account_statement{os.sep}account_statement_person.docx")
        doc.render(context)
        doc.save(f"media{os.sep}applications{os.sep}{application.id}.docx")
        # file = open(os.path.join(settings.MEDIA_ROOT, f'applications{os.sep}{application.id}.docx'), 'r').read()
        password = random.randint(1000, 9999)
        # application.file = document
        application.password = password
        application.save()

        app = serializers.serialize('json', [application, ])
        struct = json.loads(app)
        data = json.dumps(struct[0])
        return HttpResponse(data, content_type='json')
    else:
        return HttpResponse(False)


@login_required
def get_information(request):
    if request.is_ajax():
        user = get_object_or_404(User, id=request.GET.get('user'))
        application = get_object_or_404(Application, id=request.GET.get('application'))
        account_statement = get_object_or_404(AccountStatement, id=application.account_statement.id)

        context = {
            'user': f"{user.last_name} {user.first_name}",
            'passport_photo_url': user.passport_photo.url,
            'account_statement_photo_url': account_statement.cert_photo.url
        }

        data = json.dumps(context)
        return HttpResponse(data, content_type='json')
    else:
        return False
