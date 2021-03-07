from django.urls import path, include
from .views import *

app_name = 'application'

urlpatterns = [

    path('applications-list/', applications_list, name='applications_list'),
    path('application-detail/<int:id>/', application_detail, name='application_detail'),
    path('application-pdf/<int:id>/', application_pdf, name='application_pdf'),
    path('get-information/', get_information, name='get_information'),
    path('create-application-doc/<str:filename>/', create_application_doc, name='create_application_doc'),

]
