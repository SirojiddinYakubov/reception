from django.urls import path

from . import views

app_name = 'api_user'

urlpatterns = [
    path('detail/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]
