from django.urls import path, include

from . import views

app_name = 'api_user'

urlpatterns = [
    path('detail/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
    path('organizations/list/', views.UserOrganizationsList.as_view(), name='user_organizations_list'),
    path('car-models/list/', views.CarModelsList.as_view(), name='car_models_list'),
    path('car-colors/list/', views.CarColorsList.as_view(), name='car_colors_list'),
    path('car-types/list/', views.CarTypesList.as_view(), name='car_types_list'),
    path('regions/list/', views.RegionsList.as_view(), name='regions_list'),
    path('region/<int:pk>/districts/list/', views.RegionDistrictsList.as_view(), name='region_districts_list'),
    path('region/<int:pk>/sections/list/', views.RegionSectionsList.as_view(), name='region_sections_list'),
    path('district/<int:pk>/quarters/list/', views.DistrictQuartersList.as_view(), name='district_quarters_list'),
    path('car-fuel-types/list/', views.CarFuelTypesList.as_view(), name='car_fuel_types_list'),
    path('car-body-types/list/', views.CarBodyTypesList.as_view(), name='car_body_types_list'),
    path('create-organization/', views.CreateOrganization.as_view(), name='create_organization'),
    path('create-car-model/', views.CreateCarModel.as_view(), name='create_car_model'),
    path('create-color/', views.CreateColor.as_view(), name='create_color'),

    path('playmobile/sms/status/', views.PlayMobileSmsStatus.as_view()),

]
