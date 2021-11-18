from django.urls import path, include

from . import views

app_name = 'api_user'

urlpatterns = [
    path('detail/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('organizations/list/', views.UserOrganizationsList.as_view(), name='user_organizations_list'),
    path('create-organization/', views.CreateOrganization.as_view(), name='create_organization'),
    path('create-car-model/', views.CreateCarModel.as_view(), name='create_car_model'),
    path('create-color/', views.CreateColor.as_view(), name='create_color'),
]
