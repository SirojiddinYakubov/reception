from django.urls import path

from . import views

app_name = 'api_application'

urlpatterns = [
    path('create_account_statement/', views.CreateAccountStatement.as_view(), name='create_account_statement'),
    path('create_contract_of_sale/', views.CreateContractOfSale.as_view(), name='create_contract_of_sale'),
    path('create_auction_protocol/', views.CreateAuctionProtocol.as_view(), name='create_auction_protocol'),
    path('create_credit_contract/', views.CreateCreditContract.as_view(), name='create_credit_contract'),
    path('create_gift_agreement/', views.CreateGiftAgreement.as_view(), name='create_gift_agreement'),
    path('create_inheritance_agreement/', views.CreateInheritanceAgreement.as_view(),
         name='create_inheritance_agreement'),
    path('create_replace_tp/', views.CreateReplaceTp.as_view(), name='create_replace_tp'),
    path('create_replace_number_and_tp/', views.CreateReplaceNumberAndTp.as_view(),
         name='create_replace_number_and_tp'),

    path('save/application/section/<int:pk>/', views.SaveApplicationSection.as_view(), name='save_application_section'),
    path('generate-application-word/<str:filename>/', views.GenerateApplicationWord.as_view(),
         name='generate_application_word'),
    path('generate-application-pdf/<int:pk>/', views.GenerateApplicationPdf.as_view(), name='generate_application_pdf'),
    # path('application-pay-status/<int:id>/', views.ApplicationPayStatus.as_view(), name='application_pay_status'),
    path('send-application-to-section/<int:pk>/', views.SendApplicationToSection.as_view(), name='send_application_to_section'),


    path('get-payment-percents/<int:pk>/', views.GetPaymentPercents.as_view(), name='get_payment_percents'),
    path('get-payment-score/<int:application_id>/<int:percent_id>/', views.GetPaymentScore.as_view(), name='get_payment_score'),



    path('detail/<int:pk>/', views.ApplicationDetail.as_view(), name='detail'),

]
