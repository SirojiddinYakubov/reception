from django.urls import path
from django.views.generic import TemplateView

app_name = 'partners'

urlpatterns = [
    # signup, login, logout requests
    path('diagnostics-list/', TemplateView.as_view(template_name='partners/diagnostics_list.html'), name='diagnostics_list'),

]
