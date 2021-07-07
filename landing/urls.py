from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'landing'

urlpatterns = [
    # signup, login, logout requests


    # other requests
    path('', home_page, name='home_page'),

]
