from django.urls import path

from . import views

app_name = 'api_state_controller'

urlpatterns = [
    path('applications/list/', views.ApplicationsList.as_view(), name='applications_list'),
    path('payments/list/', views.PaymentsList.as_view(), name='payments_list'),
    path('state-duties/report/', views.StateDutiesReport.as_view(),
         name='state_duties_report'),
]
