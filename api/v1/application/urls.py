from django.urls import path

from . import views

app_name = 'api_application'

urlpatterns = [
    path('create_account_statement/', views.CreateAccountStatement.as_view(), name='create_account_statement'),
    path('create_contract_of_sale/', views.CreateContractOfSale.as_view(), name='create_contract_of_sale'),
    path('create_gift_agreement/', views.CreateGiftAgreement.as_view(), name='create_gift_agreement'),
    path('create_inheritance_agreement/', views.CreateInheritanceAgreement.as_view(), name='create_inheritance_agreement'),
    path('create_replace_tp/', views.CreateReplaceTp.as_view(), name='create_replace_tp'),
    path('create_replace_number_and_tp/', views.CreateReplaceNumberAndTp.as_view(), name='create_replace_number_and_tp'),

    path('save/application/section/<int:pk>/', views.SaveApplicationSection.as_view(), name='save_application_section'),
]
