from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'user'

urlpatterns = [
    # signup, login, logout requests
    path('signup/', user_signup, name='signup'),
    path('login/', login_first, name='login_first'),
    path('logout/', user_logout, name='logout'),

    # other requests
    path('', index, name='index'),
    path('edit/', edit, name='edit'),
    path('add-organization/', add_organization, name='add_organization'),
    path('view-organizations/', view_organizations, name='view_organizations'),
    path('edit-organization/<int:organization_id>/', edit_organization, name='edit_organization'),
    path('remove-organization/<int:organization_id>/', remove_organization, name='remove_organization'),

    # ajax requests
    path('get-district/', get_district, name='get_district'),
    path('get-mfy/', get_mfy, name='get_mfy'),
    path('get-code/', get_code, name='get_code'),
    path('get-user-pass/', get_user_pass, name='get_user_pass'),
    path('forgot-pass/', forgot_pass, name='forgot_pass'),
    path('get-phone/', get_phone, name='get_phone'),
    path('is-register/', is_register, name='is_register'),
    path('get-organization/', get_organization, name='get_organization'),
    # path('check_passport/', check_passport, name='check_passport'),
    # path('check_passport_with_number/', check_passport_with_number, name='check_passport_with_number'),
    path('save_user_information/', save_user_information, name='save_user_information'),
    path('upload-file/', upload_file, name='upload_file'),


]
