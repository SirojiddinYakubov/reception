from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('application/', include('api.v1.application.urls')),
    path('service/', include('api.v1.service.urls')),
    path('landing/', include('api.v1.landing.urls')),
    path('partners/', include('api.v1.partners.urls')),

    #roles
    path('app_creator/', include('api.v1.user.app_creator.urls')),
]
