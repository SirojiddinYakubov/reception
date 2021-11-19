from django.urls import path

from . import views

app_name = 'api_app_creator'

urlpatterns = [
    path('<int:pk>/organizations/list/', views.UserOrganizationsList.as_view(), name='user_organizations_list'),
    path('self-created-users/list/<int:id>/', views.SelfCreatedUsersList.as_view(), name='self_created_users_list'),
]
