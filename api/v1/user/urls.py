from django.urls import path, include

from . import views

app_name = 'api_user'

urlpatterns = [
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),

    path('login/', views.LoginView.as_view(), name='login_view'),

    path('detail/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('organizations/list/', views.UserOrganizationsList.as_view(), name='user_organizations_list'),
    path('<int:pk>/organizations/list/', views.OrganizationsList.as_view(), name='organizations_list'),
    path('car-models/list/', views.CarModelsList.as_view(), name='car_models_list'),
    path('car-colors/list/', views.CarColorsList.as_view(), name='car_colors_list'),
    path('car-types/list/', views.CarTypesList.as_view(), name='car_types_list'),
    path('devices/list/', views.DevicesList.as_view(), name='devices_list'),
    path('regions/list/', views.RegionsList.as_view(), name='regions_list'),
    path('section/exists/regions/list/', views.SectionExistsRegionsList.as_view(), name='section_exists_regions_list'),
    path('region/<int:pk>/districts/list/', views.RegionDistrictsList.as_view(), name='region_districts_list'),
    path('region/<int:pk>/sections/list/', views.RegionSectionsList.as_view(), name='region_sections_list'),
    path('district/<int:pk>/quarters/list/', views.DistrictQuartersList.as_view(), name='district_quarters_list'),
    path('car-fuel-types/list/', views.CarFuelTypesList.as_view(), name='car_fuel_types_list'),
    path('car-body-types/list/', views.CarBodyTypesList.as_view(), name='car_body_types_list'),
    path('create-organization/', views.CreateOrganization.as_view(), name='create_organization'),
    path('create-car-model/', views.CreateCarModel.as_view(), name='create_car_model'),
    path('create-color/', views.CreateColor.as_view(), name='create_color'),

    path('get-code/', views.GetCode.as_view(), name='get_code'),
    path('verify-code/', views.VerifyCode.as_view(), name='verify_code'),

    path('playmobile/sms/status/', views.PlayMobileSmsStatus.as_view()),

    path('get/card/phone/number/', views.GetCardPhoneNumber.as_view(), name='get_card_phone_number'),

    path('confirm/pay/', views.ConfirmPay.as_view(), name="confirm_pay"),

]
