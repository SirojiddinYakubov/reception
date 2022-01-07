from django.urls import path

from . import views

app_name = 'api_driver_license'

urlpatterns = [
    path('call/to/exam/send/sms/', views.CallToExamSendSms.as_view(), name='call_to_exam_send_sms'),
    path('call/to/exam/send/sms/list/', views.CallToExamSendSmsList.as_view(), name='call_to_exam_send_sms_list'),
]
