from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'account_statement'

urlpatterns = [

    #other requests
    path('insert/', insert, name='insert'),
    path('add-photo/<int:id>/', add_photo, name='add_photo'),
    path('export_to_word/<int:id>/', export_to_word, name='export_to_word'),


    #ajax requests
    path('get-car-type/', get_car_type, name='get_car_type'),


]
