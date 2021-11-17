from django.urls import path

from .payme import *

app_name = 'paycom'
urlpatterns = [
    path('api/', PayMeView.as_view(), name='api'),
    path('create-payme-order/', CreatePaymeOrder.as_view(), name='create_payme_order'),
]
