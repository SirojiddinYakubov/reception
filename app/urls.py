from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = 'app'

urlpatterns = [
    path('home/', home, name='home'),
    path('new-car/', new_car, name='new_car'),
    path('word/', word, name='word'),

]
