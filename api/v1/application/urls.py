from django.urls import path

from . import views

app_name = 'api_application'

urlpatterns = [
    path('create_account_statement/', views.CreateAccountStatement.as_view(), name='create_account_statement'),
    path('create_contract_of_sale/', views.CreateContractOfSale.as_view(), name='create_contract_of_sale'),
]
