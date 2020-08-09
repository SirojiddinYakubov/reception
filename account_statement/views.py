from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from .forms import *
from .models import *
from user.models import *
from docxtpl import DocxTemplate


# Create your views here.
def home(request):
    return render(request, 'app/home.html')


def new_car(request):
    cars = Car.objects.filter().order_by('model')
    organizations = Organization.objects.filter(director=request.user)
    context = {
        'cars': cars,
        'organizations': organizations,
    }

    if request.POST:

        form = AccountStatementForm(request.POST or None)
        print(form.errors)
        if form.is_valid():
            print(request.POST)
            form.person_type = form.cleaned_data['person_type']
            form.cert_seriya = form.cleaned_data['cert_seriya']
            form.cert_number = form.cleaned_data['cert_number']
            form.date_conclusion_contract = request.POST['organization']
            form.color = form.cleaned_data['color']
            form.engine_number = form.cleaned_data['engine_number']
            form.body_number = form.cleaned_data['body_number']
            if form.person_type == 'E':
                print('Eeee')
                form.organization = get_object_or_404(Organization, id=request.POST['organization'] or None)
            else:
                print('ppp')
            form.car = get_object_or_404(Car, id=request.POST['car'])
            form.user = User.objects.get(id=request.user.id)


            if form.car.is_truck == True:
                form.chassis_number = form.cleaned_data['chassis_number']

            form.save()



    else:
        form = AccountStatementForm()
    return render(request, 'app/new_car/home.html', context=context)


def account_statement(request):
    return False


def word(request):
    doc = DocxTemplate("static/test1.docx")
    user = User.objects.get(username=request.user.username)
    context = {
        'user': user
    }
    doc.render(context)
    doc.save("media/generated_doc.docx")


def get_car_type(request):
    if request.is_ajax():
        car_id = request.GET.get('car', None)
        car = Car.objects.get(id=car_id)
        if car.is_truck:
            message = 1
        else:
            message = 0
        return HttpResponse(message)
    else:
        return False
