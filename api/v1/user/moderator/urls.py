from django.urls import path

from . import views

app_name = 'api_moderator'

urlpatterns = [
    path('applications/list/', views.ApplicationsList.as_view(), name='applications_list'),
    path('payments/list/', views.PaymentsList.as_view(), name='payments_list'),
    path('confirm/treasury/payment/', views.ConfirmTheasuryPayment.as_view(), name='confirm_theasury_payment'),


]
