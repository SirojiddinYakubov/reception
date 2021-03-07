from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'contract_of_sale'

urlpatterns = [

    #other requests
    path('contract-of-sale-index/', contract_of_sale_index, name='contract-of-sale-index'),

    #ajax request
    path('save-contract-of-sale-and-car/', Save_Contract_Of_Sale_And_Car.as_view(), name='save_contract_of_sale_and_car'),

]
