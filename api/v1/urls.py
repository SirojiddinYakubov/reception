from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('application/', include('api.v1.application.urls')),
    path('service/', include('api.v1.service.urls')),
    path('landing/', include('api.v1.landing.urls')),
    path('partners/', include('api.v1.partners.urls')),

    #roles
    path('app_creator/', include('api.v1.user.app_creator.urls')),
    path('regional_controller/', include('api.v1.user.regional_controller.urls')),
    path('moderator/', include('api.v1.user.moderator.urls')),
    path('state_controller/', include('api.v1.user.state_controller.urls')),
]
