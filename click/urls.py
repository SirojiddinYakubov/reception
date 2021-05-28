from django.urls import path
from . import views
from .views import *

app_name = 'click'
urlpatterns = [
    path('create-order-url', create_order_url, name='create_order_url'),
    path('transaction/',TestView.as_view()),
    path('success/',success_order, name='success_order')

]