from django.urls import path

from . import views

app_name = 'api_application'

urlpatterns = [
    path('create-account-statement/', views.CreateAccountStatement.as_view(), name='create_account_statement'),
]
