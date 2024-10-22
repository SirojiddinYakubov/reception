from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('application/', include('api.v1.application.urls')),
    path('service/', include('api.v1.service.urls')),
    path('landing/', include('api.v1.landing.urls')),
    path('partners/', include('api.v1.partners.urls')),
    path('driver_license/', include('api.v1.driver_license.urls')),

    #roles
    path('app_creator/', include('api.v1.user.app_creator.urls')),
    path('regional_controller/', include('api.v1.user.regional_controller.urls')),
    path('moderator/', include('api.v1.user.moderator.urls')),
    path('state_controller/', include('api.v1.user.state_controller.urls')),
    path('checker/', include('api.v1.user.checker.urls')),
    path('administrator/', include('api.v1.user.administrator.urls')),
]
