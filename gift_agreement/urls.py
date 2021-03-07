from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'gift_agreement'

urlpatterns = [

    #other requests
    path('gift-agreement-index/', gift_agreement_index, name='gift_agreement_index'),

    #ajax request
    path('save-gift-agreement-and-car/', Save_Gift_Agreement_And_Car.as_view(), name='save_gift_agreement_and_car'),

]
