#!/usr/bin/python3


import os
import time,string
import django,random as rd

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'reception.settings')

django.setup()
#
from application.models import Application
from service.models import Service
from user.models import User, Section

def generate_application(count):
    for i in range(count):
        print(f'Generated application # {i} . . .')
        created_user = User.objects.filter(is_superuser=False).order_by('?')[0]
        service = Service.objects.all().order_by('?')[0]
        section = Section.objects.filter(parent__isnull=False).order_by('?')[0]

        Application.objects.create(
            created_user=created_user,
            service=service,
            section=section)

if __name__ == '__main__':
    generate_application(100)