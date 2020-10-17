from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy

from user.utils import render_to_pdf
from .forms import *
from .models import *
from user.models import *
from docxtpl import DocxTemplate


# Create your views here.

@login_required
def insert(request):
    cars = Car.objects.filter(is_show=True).order_by('model')
    organizations = Organization.objects.filter(created_user=request.user, is_active=True)
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
            return redirect(reverse_lazy('account_statement:add_photo', kwargs={'id': form.id}))
    else:
        form = AccountStatementForm()
    return render(request, 'account_statement/insert.html', context=context)


@login_required
def add_photo(request, id):
    data = AccountStatement.objects.get(id=id)
    context = {
        'data': data
    }
    return render(request, 'account_statement/add-photo.html', context=context)




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


