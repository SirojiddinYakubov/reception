from django.urls import path

from . import views

app_name = 'api_service'

urlpatterns = [
    path('list/', views.ServiceList.as_view(), name='services_list'),
    path('calculate/', views.Calculate.as_view(), name='calculate')
]
