from django.urls import path

from . import views

app_name = 'api_service'

urlpatterns = [
    path('list/', views.ServiceList.as_view(), name='services_list'),
]
