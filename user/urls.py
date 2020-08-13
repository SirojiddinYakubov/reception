from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'user'

urlpatterns = [
    # path('login', login, name='login'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('get-district/', get_district, name='get_district'),
    path('get-mfy/', get_mfy, name='get_mfy'),
    path('get-code/', get_code, name='get_code'),
    path('get-user-pass/', get_user_pass, name='get_user_pass'),
    path('forgot-pass/', forgot_pass, name='forgot_pass'),
    path('get-phone/', get_phone, name='get_phone'),
    path('check_passport/', check_passport, name='check_passport'),
    path('home/', panel, name='panel'),

]
