#!/usr/bin/python3


import os
import time,string
import django,random as rd

os.environ.setdefault("DJANGO_SETTINGS_MODULE",'reception.settings')

django.setup()
#
from application.models import Application
from service.models import Service
from user.models import User, Section, Organization


def generate_application(count):
    for i in range(count):

        created_user = User.objects.filter(is_superuser=False).order_by('?')[0]
        service = Service.objects.all().order_by('?')[0]
        section = Section.objects.filter(parent__isnull=False).order_by('?')[0]
        organization = Organization.objects.filter(is_active=True).first()
        application = Application.objects.create(
            created_user=created_user,
            service=service,
            section=section,
        )
        # application.person_type = 'Y' if service.organization else 'J'
        application.person_type = 'Y'
        application.save()

        service.organization = organization
        service.save()
        print(f'Fake ma\'lumotlar yaratilmoqda # {i + 1} | ID raqam: {application.id}. . .')


if __name__ == '__main__':
    generate_application(200)
