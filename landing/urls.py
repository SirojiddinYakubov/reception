from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import *
from django.conf.urls.i18n import i18n_patterns

app_name = 'landing'

urlpatterns = [
    # signup, login, logout requests


    # other requests
    path('', home_page, name='home_page'),
    path('calculate/', TemplateView.as_view(template_name='landing/calculate.html'), name='calculate'),


]

