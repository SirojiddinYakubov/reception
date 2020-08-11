from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'account_statement'

urlpatterns = [
    path('', home, name='home'),
    path('new-car/', new_car, name='new_car'),
    path('new-car/add-photo/<int:id>/', new_car_add_photo, name='new_car_add_photo'),
    path('word/', word, name='word'),
    path('get-car-type/', get_car_type, name='get_car_type'),

]