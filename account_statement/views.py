from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from .forms import *
from .models import *
from user.models import *
from docxtpl import DocxTemplate


# Create your views here.

@login_required
def home(request):
    return render(request, 'app/home.html')


@login_required
def new_car(request):
    cars = Car.objects.filter().order_by('model')
    organizations = Organization.objects.filter(director=request.user)
    context = {
        'cars': cars,
        'organizations': organizations,
    }

    if request.POST:
        form = AccountStatementForm(request.POST or None)
        if form.is_valid():
            cert_seriya = form.cleaned_data['cert_seriya']
            cert_number = form.cleaned_data['cert_number']
            color = form.cleaned_data['color']
            engine_number = form.cleaned_data['engine_number']
            body_number = form.cleaned_data['body_number']
            chassis_number = form.cleaned_data['chassis_number']
            form = form.save(commit=False)
            form.person_type = request.POST['person_type']
            form.cert_seriya = cert_seriya
            form.cert_number = cert_number
            form.date_conclusion_contract = request.POST['date_conclusion_contract']
            form.color = color
            form.engine_number = engine_number
            form.body_number = body_number

            if form.person_type == 'E':
                form.organization = get_object_or_404(Organization, id=request.POST['organization'] or None)

            form.car = get_object_or_404(Car, id=request.POST['car'])
            form.user = User.objects.get(id=request.user.id)
            if form.car.is_truck == True:
                form.chassis_number = chassis_number
            form.save()
            print(form.id)
            # return HttpResponseRedirect(reverse('account_statement:new_car_add_photo', id=form.id))
            return redirect(reverse_lazy('account_statement:new_car_add_photo', kwargs={'id': form.id}))
    else:
        form = AccountStatementForm()
    return render(request, 'app/new_car/add-form.html', context=context)


@login_required
def new_car_add_photo(request, id):
    data = AccountStatement.objects.get(id=id)
    context = {
        'data': data
    }
    return render(request, 'app/new_car/add-photo.html', context=context)


@login_required
def account_statement(request):
    return False


@login_required
def word(request):
    doc = DocxTemplate("static/test1.docx")
    user = User.objects.get(username=request.user.username)
    context = {
        'user': user
    }
    doc.render(context)
    doc.save("media/generated_doc.docx")


@login_required
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
