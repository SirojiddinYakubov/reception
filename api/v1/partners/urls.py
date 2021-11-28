from django.urls import path

from . import views

app_name = 'api_partners'

urlpatterns = [
    path('district/<int:pk>/diagnostics/list/', views.DistrictDiagnosticsList.as_view(), name='district_diagnostics_list'),
]
