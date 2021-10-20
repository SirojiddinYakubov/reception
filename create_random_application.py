#!/usr/bin/python3

import os
import time, string
from datetime import datetime

import django, random as rd

os.environ.setdefault("DJANGO_SETTINGS_MODULE", 'reception.settings')

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
        application.person_type = 1
        application.save()

        service.organization = organization
        service.save()
        print(f'Fake ma\'lumotlar yaratilmoqda # {i + 1} | ID raqam: {application.id}. . .')

def decorator(decorator_params):
    if callable(decorator_params):
        def wrapper(*args, **kwargs):
            start = datetime.now()
            result = decorator_params(*args, **kwargs)
            print(datetime.now() - start)
            return result
        return wrapper
    else:
        def extra_params(func):
            def wrapper(*args, **kwargs):
                start = datetime.now()
                result = func(decorator_params)
                print(datetime.now() - start)
                return result
            return wrapper
        return extra_params




@decorator
def one(n):
    l = []
    for i in range(n):
        if i % 2 == 0:
            l.append(i)
    return l

@decorator
def two(n):
    return [x for x in range(n) if x % 2 == 0]

def countdown(n):
    result = []
    while n != 0:
        result.append(n)
        n -= 1
    return result

def gen_countdown(n):
    while n != 0:
        yield n
        n -= 1

def gen_func(n):
    result = []
    while n != 0:
        result.append(n)
        n -= 1
    yield result

if __name__ == '__main__':
    # generate_application(200)
    # one(10**5)
    # two(10**5)
    # g = gen_countdown(5)
    g = gen_func(5)
    print(g)

