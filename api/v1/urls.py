from django.urls import path, include

urlpatterns = [
    path('user/', include('api.v1.user.urls')),
    path('application/', include('api.v1.application.urls')),

    #roles
    path('app_creator/', include('api.v1.user.app_creator.urls')),
]
