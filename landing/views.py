from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
# Create your views here.
from django.urls import reverse_lazy
from django.utils import translation
from django.views import generic

from landing.models import Vacancy


def home_page(request):
    request.META.get('HTTP_ACCEPT_LANGUAGE', '')
    # print(request.META)
    # if request.path == '/ru/':
    #     translation.activate('ru')
    #     request.session['lang'] = 'ru'
    #
    # elif request.path == '/uz/':
    #     translation.activate('uz')
    #     request.session['lang'] = 'uz'
    # elif request.path == '/en/':
    #     translation.activate('en')
    #     request.session['lang'] = 'en'
    return render(request, 'landing/index.html')


class VacancyList(generic.ListView):
    template_name = 'landing/vacancy_list.html'
    queryset = Vacancy.objects.filter(is_active=True)
    context_object_name = 'vacancy_list'

class VacancyDetail(generic.DetailView):
    template_name = 'landing/vacancy_detail.html'
    model = Vacancy
    context_object_name = 'vacancy'
