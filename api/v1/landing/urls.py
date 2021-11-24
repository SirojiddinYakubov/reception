from django.urls import path

from . import views

app_name = 'api_landing'

urlpatterns = [
    path('calculate/', views.Calculate.as_view(), name='calculate'),
]
