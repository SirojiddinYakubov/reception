from django.urls import path, include
from django.views.generic import TemplateView

from .views import *

app_name = 'application'

urlpatterns = [

    path('application/', applications_list, name='applications_list'),
    path( 'applications', TemplateView.as_view(template_name='user/role/state_controller/applications_list.html'), name='applications'),
    path('applications-list/', ApplicationsList.as_view(), name='ApplicationsList'),

    path('application-detail/<int:id>/', application_detail, name='application_detail'),
    path('application-pdf/<int:id>/', application_pdf, name='application_pdf'),
    path('get-information/', get_information, name='get_information'),
    path('create-application-doc/<str:filename>/', create_application_doc, name='create_application_doc'),
    path('view-service-data/<int:service_id>/', view_service_data, name='view_service_data'),

    path('change-get-request/<str:key>/<str:value>/', change_get_request, name='change_get_request'),
    path('confirm-application-data/', ConfirmApplicationData.as_view(), name='confirm_application_data'),
    path('get-given-number/<int:id>/', GetGivenNumber.as_view(), name='get_given_number'),
    path('remove-application/', RemoveApplication.as_view(), name='remove_application'),

    path('payment-detail/<int:service_id>/', payment_detail, name='payment_detail'),
    path('payments/', payments, name='payments'),
    path('modify-payment-checkbox/', Modify_Payment_Checkbox.as_view(), name='modify_payment_checkbox'),

    path('generate-qr-code-image/<int:id>/', generate_qr_code_image, name='generate_qr_code_image'),

    path('check-application-status/<int:id>/', check_application_status, name='check_application_status'),

    path('access-with-qrcode/<int:id>/', access_with_qrcode, name='access_with_qrcode'),

]
