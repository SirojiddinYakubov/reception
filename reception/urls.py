"""reception URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from reception import settings
from user.views import HelloView, CustomAuthToken
from django.conf.urls.i18n import i18n_patterns


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('yoz/', admin.site.urls),
    path('sentry-debug/', trigger_error),

    path('api/v1/', include('api.v1.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('payme/', include('paycom.urls')),
    path('click/', include('click.urls')),
    path('payments/', include('payments.urls')),

]

urlpatterns += i18n_patterns(
    path('service/', include('service.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('landing.urls')),
    path('user/', include('user.urls')),
    path('application/', include('application.urls')),
    path('error-403/', TemplateView.as_view(template_name='_parts/403.html', ),
         name='error_403'),

)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = "user.views.handler404"
