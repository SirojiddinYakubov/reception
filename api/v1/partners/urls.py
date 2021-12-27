from django.urls import path

from . import views

app_name = 'api_partners'

urlpatterns = [
    path('diagnostics/list/', views.DiagnosticsList.as_view(), name='diagnostics_list'),
]
