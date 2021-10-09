from datetime import timedelta

from django.db.models import Q
from django.utils import timezone

from application.models import Application
from reception.api import SendSmsWithApi
from application.models import (
CREATED,
ACCEPTED_FOR_CONSIDERATION
)

def application_crontab():
    applications = Application.objects.filter(Q(is_active=True) & Q(process__in=[CREATED, ACCEPTED_FOR_CONSIDERATION]))

    for application in applications:
        # Faollashtirilmagan arizalar

        # ariza jarayonda lekin ariza faollashtirilmagan. 3 kun davomida
        if application.process == CREATED and application.cron == '1' and application.is_block and timezone.now() - timedelta(
                days=3) > application.created_date:
            application.cron = '2'
            application.save()
            text = f'Hurmatli foydalanuvchi {application.id}-raqamli arizangiz faollashtirilmaganligi eslatib o\'tamiz! Arizani faollashtirish uchun kerakli to\'lovni amalga oshirish talab etiladi!'
            SendSmsWithApi(message=text, phone=application.created_user.phone)

        # ariza jarayonda lekin ariza faollashtirilmagan. 7 kun davomida
        if application.process == CREATED and application.cron == '2' and application.is_block and timezone.now() - timedelta(
                days=7) > application.created_date:
            application.cron = '3'
            application.save()

            text = f'Hurmatli foydalanuvchi {application.id}-raqamli arizangiz faollashtirilmaganligi eslatib o\'tamiz! Agarda 3 kun davomida arizani faollashtirmasangiz arizangiz o\'chirib yuboriladi'
            SendSmsWithApi(message=text, phone=application.created_user.phone)

        # ariza jarayonda lekin ariza faollashtirilmagan. 10 kun davomida
        if application.process == CREATED and application.cron == '3' and application.is_block and timezone.now() - timedelta(
                days=10) > application.created_date:
            application.delete()
            text = f'Hurmatli foydalanuvchi {application.id}-raqamli arizangiz faollashtirilmaganligi sababli e-rib tzimidan o\'chirildi!'
            SendSmsWithApi(message=text, phone=application.created_user.phone)

        # Faollashtirilgan lekin hech qanday amaliyot amalga oshirilmagan arizalar

        # ariza jarayonda lekin 3 kun davomida hech qanday amaliyot bajarilmagan
        if application.process == ACCEPTED_FOR_CONSIDERATION and not application.service.car.is_confirm and not application.service.car.is_technical_confirm and application.cron == '1' and not application.is_block and timezone.now() - timedelta(
                days=3) > application.created_date:
            application.cron = '2'
            application.save()
            text = f'Hurmatli foydalanuvchi {application.id}-raqamli arizangiz bilan hech qanday amaliyot amalga oshirilmagan!'
            SendSmsWithApi(message=text, phone=application.created_user.phone)

        # ariza jarayonda lekin 7 kun davomida hech qanday amaliyot bajarilmagan
        if application.process == ACCEPTED_FOR_CONSIDERATION and not application.service.car.is_confirm and not application.service.car.is_technical_confirm and application.cron == '2' and not application.is_block and timezone.now() - timedelta(
                days=7) > application.created_date:
            application.cron = '3'
            application.save()
            text = f'Hurmatli foydalanuvchi {application.id}-raqamli arizangiz bilan hech qanday amaliyot amalga oshirmaganligingiz sababli ogohlantirish beramiz! Agarda 3 kun davomida ariza bilan hech qanday amaliyot amalga oshirmasangiz arizangiz o\'chirib yuboriladi'
            SendSmsWithApi(message=text, phone=application.created_user.phone)

        # ariza jarayonda lekin 10 kun davomida hech qanday amaliyot bajarilmagan
        if application.process == ACCEPTED_FOR_CONSIDERATION and not application.service.car.is_confirm and not application.service.car.is_technical_confirm and application.cron == '3' and not application.is_block and timezone.now() - timedelta(
                days=10) > application.created_date:
            application.delete()

            text = f'Hurmatli foydalanuvchi {application.id}-raqamli arizangiz hech qanday amaliyot amalga oshirmaganligingiz sababli e-rib tizimidan o\'chirildi!'
            SendSmsWithApi(message=text, phone=application.created_user.phone)


        # Rad etilgan ariza 60 kundan so'ng o'chirib yuboriladi
        if application.process == '3' and not application.is_block and timezone.now() - timedelta(
                days=60) > application.created_date:
            application.delete()
