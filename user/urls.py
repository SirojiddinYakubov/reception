from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'user'

urlpatterns = [
    # signup, login, logout requests
    path('signup/', user_signup, name='signup'),
    path('login/', login_first, name='login_first'),
    path('logout/', user_logout, name='logout'),
    path('custom-logout/', Logout.as_view(), name='custom_logout'),

    # other requests
    path('', personal_data, name='personal_data'),
    path('edit-personal-data/', edit_personal_data, name='edit_personal_data'),
    path('add-organization/', add_organization, name='add_organization'),
    path('organizations-list/', organizations_list, name='organizations_list'),
    path('edit-organization/<int:organization_id>/', edit_organization, name='edit_organization'),
    path('remove-organization/', Remove_Organization.as_view(), name='remove_organization'),

    # ajax requests
    path('get-district/', get_district, name='get_district'),
    path('get-mfy/', get_mfy, name='get_mfy'),
    path('get-code/', get_code, name='get_code'),
    path('get-user-pass/', get_user_pass, name='get_user_pass'),
    path('forgot-pass/', forgot_pass, name='forgot_pass'),
    path('get-phone/', get_phone, name='get_phone'),
    path('is-register/', is_register, name='is_register'),
    path('get-organization/', Get_Organization.as_view(), name='get_organization'),
    # path('check_passport/', check_passport, name='check_passport'),
    # path('check_passport_with_number/', check_passport_with_number, name='check_passport_with_number'),
    path('save-user-information/', Save_User_Information.as_view(), name='save_user_information'),
    path('save-passport-data/', save_passport_data.as_view(), name='save_passport_data'),
    path('add-worker/', add_worker, name='add_worker'),
    path('workers-list/', workers_list, name='workers_list'),
    path('worker-delete/<int:worker_id>/', worker_delete, name='worker_delete'),
    path('worker-edit/<int:worker_id>/', worker_edit, name='worker_edit'),

    # ajax requests
    path('get-car-type/', Get_Car_Type.as_view(), name='get_car_type'),


]
