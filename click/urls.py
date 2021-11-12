from django.urls import path
from . import views

app_name = 'click'
urlpatterns = [
    path('create-click-order', views.CreateClickOrder.as_view(), name='create_click_order'),
    path('transaction/', views.TestView.as_view()),
    path('success/', views.success_order, name='success_order')

]
