from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'customs_certificate'

urlpatterns = [

    #other requests
    path('customs-certificate-index/', customs_certificate_index, name='customs_certificate_index'),

    #ajax request
    path('save-customs-certificate-and-car/', Save_Custom_Certificate_And_Car.as_view(), name='save_customs_certificate_and_car'),

]
