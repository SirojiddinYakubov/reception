from django.urls import path, include
from .views import *

app_name = 'application'

urlpatterns = [

    path('index/', index, name='index'),
    path('detail/', detail, name='detail'),

    path('save-application-information/', save_application_information, name='save_application_information'),
    path('get-information/', get_information, name='get_information'),

]
