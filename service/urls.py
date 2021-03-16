from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'service'

urlpatterns = [
    path('account-statement-index/', account_statement_index, name='account_statement_index'),
    path('save-account-statement/', Save_Account_Statement.as_view(), name='save_account_statement'),

    path('gift-agreement-index/', gift_agreement_index, name='gift_agreement_index'),
    path('save-gift-agreement/', Save_Gift_Agreement.as_view(), name='save_gift_agreement'),

    path('contract-of-sale-index/', contract_of_sale_index, name='contract_of_sale_index'),
    path('save-contract-of-sale/', Save_Contract_Of_Sale.as_view(), name='save_contract_of_sale'),

]
