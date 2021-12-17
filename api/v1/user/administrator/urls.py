from django.urls import path

from . import views

app_name = 'api_administrator'

urlpatterns = [
    path('applicants/list/', views.ApplicantsList.as_view(), name='applicants_list'),
    path('account/balance/', views.AccountBalance.as_view(), name='account_balance'),

]
