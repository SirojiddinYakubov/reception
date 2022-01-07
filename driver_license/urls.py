from django.urls import path
from django.views.generic import TemplateView

app_name = 'driver_license'

urlpatterns = [
    path('call/to/exam/', TemplateView.as_view(template_name='driver_license/call_to_exam.html'), name='call_to_exam'),
    path('call/to/exam/list/', TemplateView.as_view(template_name='driver_license/call_to_exam_list.html'), name='call_to_exam_list'),

]
