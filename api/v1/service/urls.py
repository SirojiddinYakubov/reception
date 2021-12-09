from django.urls import path

from . import views

app_name = 'api_service'

urlpatterns = [
    path('list/', views.ServiceList.as_view(), name='services_list'),
    path('state-duty-percent/detail/<int:pk>/', views.StateDutyPercentDetail.as_view(),
         name='state_duty_percent_detail'),
    path('state-duties/list/', views.StateDutiesList.as_view(), name='state_duties_list'),
    path('payment-for-treasury/list/', views.PaymentForTreasuryList.as_view(), name='payment_for_treasury_list'),

]
