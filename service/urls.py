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

    path('replace-tp-index/', replace_tp_index, name='replace_tp_index'),
    path('save-replace-tp/', Save_Replace_Tp.as_view(), name='save_replace_tp'),

    path('replace-number-and-tp-index/', replace_number_and_tp_index, name='replace_number_and_tp_index'),
    path('save-replace-number-and-tp/', Save_Replace_Number_And_Tp.as_view(), name='save_replace_number_and_tp'),

    path('re-equipment-index/', re_equipment_index, name='re_equipment_index'),
    path('save-re-equipment/', Save_Re_Equipment.as_view(), name='save_re_equipment'),




    path('modify-payment-checkbox/', Modify_Payment_Checkbox.as_view(), name='modify_payment_checkbox'),
]
