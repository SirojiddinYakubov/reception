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

from reception import settings
from user.views import HelloView, CustomAuthToken
from django.conf.urls.i18n import i18n_patterns


def trigger_error(request):
    division_by_zero = 1 / 0


def test(request):
    print(request)
    return HttpResponse(request)


urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),
    path('hello/', HelloView.as_view(), name='hello'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('auth/', include('djoser.urls.jwt')),
    # path('api-token-auth/', CustomAuthToken.as_view(), name='api_token_auth'),
    path('payme/', include('paycom.urls')),
    path('click/', include('click.urls')),
    path('payments/', include('payments.urls')),
    path('test/', test),

]

urlpatterns += i18n_patterns(
    path('service/', include('service.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('user.urls')),
    path('application/', include('application.urls')),
    path('error-403/', TemplateView.as_view(template_name='_parts/403.html', ),
         name='error_403'),

)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404="user.views.handler404"