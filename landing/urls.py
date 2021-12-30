from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from . import views
from django.conf.urls.i18n import i18n_patterns

app_name = 'landing'

urlpatterns = [
    # signup, login, logout requests


    # other requests
    path('', views.home_page, name='home_page'),
    path('calculate/', TemplateView.as_view(template_name='landing/calculate.html'), name='calculate'),
    path('diagnostics/', TemplateView.as_view(template_name='landing/diagnostics.html'), name='diagnostics'),
    path('vacancy/', views.VacancyList.as_view(), name='vacancy_list'),
    path('vacancy/detail/<int:pk>/', views.VacancyDetail.as_view(), name='vacancy_detail'),

]

