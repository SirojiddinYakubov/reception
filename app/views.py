from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from user.models import *
from docxtpl import DocxTemplate


# Create your views here.
def home(request):
    return render(request, 'app/home.html')


def new_car(request):
    cars = Car.objects.filter().order_by('model')
    context = {
        'cars': cars,
    }
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


