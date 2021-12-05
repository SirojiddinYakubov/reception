from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

from .views import *

app_name = 'user'

urlpatterns = [
    # signup, login, logout requests
    path('signup/', user_signup, name='signup'),
    path('login/', TemplateView.as_view(template_name='account/login.html'),
         name='login_view'),
    path('logout/', user_logout, name='logout'),
    path('custom-logout/', Logout.as_view(), name='custom_logout'),
    path('handler404/', handler404, name='handler404'),

    # other requests
    path('home/', Home.as_view(), name='home'),
    path('', personal_data, name='personal_data'),
    path('view-personal-data/<int:id>/', view_personal_data, name='view_personal_data'),
    path('edit-personal-data/', EditPersonalData.as_view(), name='edit_personal_data'),
    path('save-personal-data/', SavePersonalData.as_view(), name='save_personal_data'),
    path('add-organization/', add_organization, name='add_organization'),

    path('organizations-list/', OrganizationList.as_view(), name='organizations_list'),
    path('edit-organization/<int:organization_id>/', edit_organization, name='edit_organization'),
    path('remove-organization/', Remove_Organization.as_view(), name='remove_organization'),

    # ajax requests
    path('get-district/', get_district, name='get_district'),
    path('get-child-sections/', GetChildSections.as_view(), name='GetChildSections'),

    path('get-code/', GetCode.as_view(), name='get_code'),
    path('verify-code/', VerifyCode.as_view(), name='verify_code'),
    path('get-user-pass/', get_user_pass, name='get_user_pass'),
    path('forgot-pass/', forgot_pass, name='forgot_pass'),
    path('get-phone/', get_phone, name='get_phone'),
    path('is-register/', is_register, name='is_register'),
    path('get-organization/', Get_Organization.as_view(), name='get_organization'),
    # path('check_passport/', check_passport, name='check_passport'),
    # path('check_passport_with_number/', check_passport_with_number, name='check_passport_with_number'),
    path('save-user-information/', SaveUserInformation.as_view(), name='save_user_information'),
    path('save-user-passport/<int:pk>/', SaveUserPassport.as_view(), name='save_user_passport'),
    path('add-worker/', add_worker, name='add_worker'),
    path('workers-list/', workers_list, name='workers_list'),
    path('worker-delete/<int:worker_id>/', worker_delete, name='worker_delete'),
    path('worker-edit/<int:worker_id>/', worker_edit, name='worker_edit'),
    # path('view-car-data/<int:car_id>/', view_car_data, name='view_car_data'),
    path('view-car-data/<int:car_id>/', ViewCarData.as_view(), name='view_car_data'),
    # path('edit-car-data/<int:car_id>/', edit_car_data, name='edit_car_data'),
    path('edit-car-data/<int:car_id>/', EditCarData.as_view(), name='edit_car_data'),
    path('view-organization-data/<int:id>/', view_organization_data, name='view_organization_data'),
    path('confirm-car-data/<int:car_id>/', confirm_car_data, name='confirm_car_data'),

    # ajax requests
    path('get-car-type/', Get_Car_Type.as_view(), name='get_car_type'),
    path('save-new-car-model/', Save_New_Car_Model.as_view(), name='save_new_car_model'),
    path('save-new-color/', Save_New_Color.as_view(), name='save_new_color'),
    path('getDistricts/', getDistricts, name='getDistricts'),
    path('getQuarters/', getQuarters, name='getQuarters'),
    path('get_quarters/', get_quarters, name='get_quarters'),

    # STATE CONTROLLER
    path('regions-list/', regions_list, name='regions_list'),
    path('sections-list/<int:section_id>/', sections_list, name='sections_list'),
    path('sections-list-by-region/', SectionsListByRegion.as_view(), name='sections_list_by_region'),
    path('get-regions-list/', GetRegionsList.as_view(), name='get_regions_list'),
    path('get-sections-list/<int:region_id>/', GetSectionsList.as_view(), name='get_sections_list'),

    # path('section-districts-list/<int:section_id>/', section_districts_list, name='section_districts_list'),

    # app creatoe role
    path('create_user_account_view/', CreateUserAccountView.as_view(), name='create_user_account_view'),

    path('create/card/pay/', TemplateView.as_view(template_name='payments/apelsin.html'), name="create_card_pay")
]
