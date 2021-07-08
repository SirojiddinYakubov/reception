from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from django.utils import translation


def home_page(request):
    if request.path == '/ru/':
        translation.activate('ru')
        request.session['lang'] = 'ru'

    elif request.path == '/uz/':
        translation.activate('uz')
        request.session['lang'] = 'uz'
    elif request.path == '/en/':
        translation.activate('en')
        request.session['lang'] = 'en'
    return render(request, 'landing/index.html')
