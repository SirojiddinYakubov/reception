from django.http import HttpResponse
from django.shortcuts import render
from .models import *
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


def word(request):
    doc = DocxTemplate("static/test1.docx")
    context = {'current_year': "2020"}
    doc.render(context)
    doc.save("media/generator/generated_doc.docx")


