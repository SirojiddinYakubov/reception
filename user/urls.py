from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'user'

urlpatterns = [
    # path('login', login, name='login'),
    path('sign', sign, name='sign'),
    path('get-district/', get_district, name='get_district'),
    path('get-mfy/', get_mfy, name='get_mfy'),
    path('get-code/', get_code, name='get_code'),
    path('check_passport/', check_passport, name='check_passport'),
    path('panel/', panel, name='panel'),

]
