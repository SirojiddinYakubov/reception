from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'account_statement'

urlpatterns = [

    #other requests
    path('account-statement-insert/', account_statement_insert, name='account_statement_insert'),
    path('save-account-statement-and-car/', Save_Account_Statement_And_Car.as_view(), name='save_account_statement_and_car'),
    path('add-photo/<int:id>/', add_photo, name='add_photo'),
    path('export_to_word/<int:id>/', export_to_word, name='export_to_word'),





]
