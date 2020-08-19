from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'user'

urlpatterns = [
    # signup, login, logout requests
    path('signup/', user_signup, name='signup'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),

    #other requests
    path('', index, name='index'),

    # ajax requests
    path('get-district/', get_district, name='get_district'),
    path('get-mfy/', get_mfy, name='get_mfy'),
    path('get-code/', get_code, name='get_code'),
    path('get-user-pass/', get_user_pass, name='get_user_pass'),
    path('forgot-pass/', forgot_pass, name='forgot_pass'),
    path('get-phone/', get_phone, name='get_phone'),
    path('check_passport/', check_passport, name='check_passport'),

]
