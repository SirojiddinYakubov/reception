from datetime import timedelta

from django.db.models import Q
from django.utils import timezone

from application.models import Application


def application_crontab():
    applications = Application.objects.filter(Q(is_active=True) & Q(process__in=['1', '3']))

    for application in applications:
        # Faollashtirilmagan arizalar

        # ariza jarayonda lekin ariza faollashtirilmagan. 3 kun davomida
        if application.process == '1' and application.cron == '1' and application.is_block and timezone.now() - timedelta(
                days=3) > application.created_date:
            application.cron = '2'
            application.save()
            # print(f'Hurmatli foydalanuvchi {application.id}-raqamli arizangiz faollashtirilmaganligi eslatib o\'tamiz! Arizani faollashtirish uchun kerakli to'lovni amalga oshirish talab etiladi!')

        # ariza jarayonda lekin ariza faollashtirilmagan. 7 kun davomida
        if application.process == '1' and application.cron == '2' and application.is_block and timezone.now() - timedelta(
                days=7) > application.created_date:
            application.cron = '3'
            application.save()

            # print(f'Hurmatli foydalanuvchi {application.id}-raqamli arizangiz faollashtirilmaganligi eslatib o\'tamiz! Agarda 3 kun davomida arizani faollashtirmasangiz arizangiz o\'chirib yuboriladi')

        # ariza jarayonda lekin ariza faollashtirilmagan. 10 kun davomida
        if application.process == '1' and application.cron == '3' and application.is_block and timezone.now() - timedelta(
                days=10) > application.created_date:
            application.delete()
            # print(f'Hurmatli foydalanuvchi {application.id}-raqamli arizangiz faollashtirilmaganligi sababli e-rib tzimidan o'chirildi!')

        # Faollashtirilgan lekin hech qanday amaliyot amalga oshirilmagan arizalar

        # ariza jarayonda lekin 3 kun davomida hech qanday amaliyot bajarilmagan
        if application.process == '1' and not application.service.car.is_confirm and not application.service.car.is_technical_confirm and application.cron == '1' and not application.is_block and timezone.now() - timedelta(
                days=3) > application.created_date:
            application.cron = '2'
            application.save()
            # print(f'Hurmatli foydalanuvchi {application.id}-raqamli arizangiz bilan hech qanday amaliyot amalga oshirilmagan!')

        # ariza jarayonda lekin 7 kun davomida hech qanday amaliyot bajarilmagan
        if application.process == '1' and not application.service.car.is_confirm and not application.service.car.is_technical_confirm and application.cron == '2' and not application.is_block and timezone.now() - timedelta(
                days=7) > application.created_date:
            application.cron = '3'
            application.save()
            # print(f'Hurmatli foydalanuvchi {application.id}-raqamli arizangiz bilan hech qanday amaliyot amalga oshirmaganligingiz sababli ogohlantirish beramiz! Agarda 3 kun davomida ariza bilan hech qanday amaliyot amalga oshirmasangiz arizangiz o\'chirib yuboriladi')

        # ariza jarayonda lekin 10 kun davomida hech qanday amaliyot bajarilmagan
        if application.process == '1' and not application.service.car.is_confirm and not application.service.car.is_technical_confirm and application.cron == '3' and not application.is_block and timezone.now() - timedelta(
                days=10) > application.created_date:
            application.delete()

            # print(f'Hurmatli foydalanuvchi {application.id}-raqamli arizangiz hech qanday amaliyot amalga oshirmaganligingiz sababli e-rib tzimidan o'chirildi!')

        # Rad etilgan ariza 60 kundan so'ng o'chirib yuboriladi
        if application.process == '3' and not application.is_block and timezone.now() - timedelta(
                days=60) > application.created_date:
            application.delete()
