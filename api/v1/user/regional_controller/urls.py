from django.urls import path

from . import views

app_name = 'api_regional_controller'

urlpatterns = [
    path('applications/list/', views.ApplicationsList.as_view(), name='applications_list'),

]
