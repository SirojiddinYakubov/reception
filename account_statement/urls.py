from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'account_statement'

urlpatterns = [
    path('', home, name='home'),
    path('account-statement/insert/', insert, name='insert'),
    path('account-statement/add-photo/<int:id>/', add_photo, name='add_photo'),
    path('account-statement/export_to_word/<int:id>/', export_to_word, name='export_to_word'),
    path('account-statement/get-car-type/', get_car_type, name='get_car_type'),

]
