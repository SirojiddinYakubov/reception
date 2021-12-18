# from datetime import timedelta
#
# from django.db.models import Q
# from django.utils import timezone
#
# from application.models import Application
# from reception.api import SendSmsWithApi, SendSmsWithPlayMobile, SUCCESS, PaymentByRequisites
# from application.models import (
#     CREATED,
#     ACCEPTED_FOR_CONSIDERATION
# )
# from reception.telegram_bot import send_message_to_developer
# from user.models import Balance


def application_crontab():
    print('HELLO')
    # applications = Application.objects.filter(Q(is_active=True) & Q(process__in=[CREATED, ACCEPTED_FOR_CONSIDERATION]))

    # for application in applications:
    #     # Faollashtirilmagan arizalar
    #
    #     # activ holatda bo'lmagan arizalarni bazadan o'chirish
    #     if timezone.now() - timedelta(days=3) > application.created_date and not application.is_active:
    #         application.delete()
    #
    #     # ariza jarayonda lekin ariza faollashtirilmagan. 3 kun davomida
    #     if application.process == CREATED and application.cron == '1' and application.is_block and timezone.now() - timedelta(
    #             days=3) > application.created_date:
    #         application.cron = '2'
    #         application.save()
    #         text = f'E-RIB.UZ: Hurmatli foydalanuvchi {application.id}-raqamli arizangiz faollashtirilmaganligi eslatib o\'tamiz! Arizani faollashtirish uchun kerakli to\'lovni amalga oshirish talab etiladi! Qo\'shimcha ma\'lumot uchun tel:972800809'
    #
    #         r = SendSmsWithPlayMobile(phone=application.created_user.phone, message=text).get()
    #         print(text)
    #         if not r == SUCCESS:
    #             # send sms with eskiz
    #             r = SendSmsWithApi(message=text, phone=application.created_user.phone).get()
    #
    #         if r != SUCCESS:
    #             send_message_to_developer(f'Sms service not working!')
    #
    #
    #     # ariza jarayonda lekin ariza faollashtirilmagan. 7 kun davomida
    #     if application.process == CREATED and application.cron == '2' and application.is_block and timezone.now() - timedelta(
    #             days=7) > application.created_date:
    #         application.cron = '3'
    #         application.save()
    #
    #         text = f'E-RIB.UZ: Hurmatli foydalanuvchi {application.id}-raqamli arizangiz faollashtirilmaganligi eslatib o\'tamiz! Agarda 3 kun davomida arizani faollashtirmasangiz arizangiz o\'chirib yuboriladi! Qo\'shimcha ma\'lumot uchun tel:972800809'
    #         r = SendSmsWithPlayMobile(phone=application.created_user.phone, message=text).get()
    #         print(text)
    #         if not r == SUCCESS:
    #             # send sms with eskiz
    #             r = SendSmsWithApi(message=text, phone=application.created_user.phone).get()
    #
    #         if r != SUCCESS:
    #             send_message_to_developer(f'Sms service not working!')
    #
    #     # ariza jarayonda lekin ariza faollashtirilmagan. 10 kun davomida
    #     if application.process == CREATED and application.cron == '3' and application.is_block and timezone.now() - timedelta(
    #             days=10) > application.created_date:
    #         application.delete()
    #         text = f'E-RIB.UZ: Hurmatli foydalanuvchi {application.id}-raqamli arizangiz faollashtirilmaganligi sababli e-rib tzimidan o\'chirildi! Qo\'shimcha ma\'lumot uchun tel:972800809'
    #         r = SendSmsWithPlayMobile(phone=application.created_user.phone, message=text).get()
    #         print(text)
    #         if not r == SUCCESS:
    #             # send sms with eskiz
    #             r = SendSmsWithApi(message=text, phone=application.created_user.phone).get()
    #
    #         if r != SUCCESS:
    #             send_message_to_developer(f'Sms service not working!')
    #
    #     # Faollashtirilgan lekin hech qanday amaliyot amalga oshirilmagan arizalar
    #
    #     # ariza jarayonda lekin 3 kun davomida hech qanday amaliyot bajarilmagan
    #     if application.process == ACCEPTED_FOR_CONSIDERATION and not application.service.car.is_confirm and not application.service.car.is_technical_confirm and application.cron == '1' and not application.is_block and timezone.now() - timedelta(
    #             days=3) > application.created_date:
    #         application.cron = '2'
    #         application.save()
    #         text = f'E-RIB.UZ: Hurmatli foydalanuvchi {application.id}-raqamli arizangiz bilan hech qanday amaliyot amalga oshirilmagan! Qo\'shimcha ma\'lumot uchun tel:972800809'
    #         r = SendSmsWithPlayMobile(phone=application.created_user.phone, message=text).get()
    #         print(text)
    #         if not r == SUCCESS:
    #             # send sms with eskiz
    #             r = SendSmsWithApi(message=text, phone=application.created_user.phone).get()
    #
    #         if r != SUCCESS:
    #             send_message_to_developer(f'Sms service not working!')
    #
    #     # ariza jarayonda lekin 7 kun davomida hech qanday amaliyot bajarilmagan
    #     if application.process == ACCEPTED_FOR_CONSIDERATION and not application.service.car.is_confirm and not application.service.car.is_technical_confirm and application.cron == '2' and not application.is_block and timezone.now() - timedelta(
    #             days=7) > application.created_date:
    #         application.cron = '3'
    #         application.save()
    #         text = f'E-RIB.UZ: Hurmatli foydalanuvchi {application.id}-raqamli arizangiz bilan hech qanday amaliyot amalga oshirmaganligingiz sababli ogohlantirish beramiz! Agarda 3 kun davomida ariza bilan hech qanday amaliyot amalga oshirmasangiz arizangiz o\'chirib yuboriladi! Qo\'shimcha ma\'lumot uchun tel:972800809'
    #         r = SendSmsWithPlayMobile(phone=application.created_user.phone, message=text).get()
    #         print(text)
    #         if not r == SUCCESS:
    #             # send sms with eskiz
    #             r = SendSmsWithApi(message=text, phone=application.created_user.phone).get()
    #
    #         if r != SUCCESS:
    #             send_message_to_developer(f'Sms service not working!')
    #
    #     # ariza jarayonda lekin 10 kun davomida hech qanday amaliyot bajarilmagan
    #     if application.process == ACCEPTED_FOR_CONSIDERATION and not application.service.car.is_confirm and not application.service.car.is_technical_confirm and application.cron == '3' and not application.is_block and timezone.now() - timedelta(
    #             days=10) > application.created_date:
    #         application.delete()
    #
    #         text = f'E-RIB.UZ: Hurmatli foydalanuvchi {application.id}-raqamli arizangiz hech qanday amaliyot amalga oshirmaganligingiz sababli e-rib tizimidan o\'chirildi! Qo\'shimcha ma\'lumot uchun tel:972800809'
    #         r = SendSmsWithPlayMobile(phone=application.created_user.phone, message=text).get()
    #         print(text)
    #         if not r == SUCCESS:
    #             # send sms with eskiz
    #             r = SendSmsWithApi(message=text, phone=application.created_user.phone).get()
    #
    #         if r != SUCCESS:
    #             send_message_to_developer(f'Sms service not working!')
    #
    #     # Rad etilgan ariza 60 kundan so'ng o'chirib yuboriladi
    #     if application.process == '3' and not application.is_block and timezone.now() - timedelta(
    #             days=60) > application.created_date:
    #         application.delete()


    # #account balansini olish
    # account_balance = PaymentByRequisites().account_balance()
    # if account_balance['status'] == SUCCESS:
    #     balance = int(account_balance['result']) / 100
    #     Balance.objects.create(amount=balance)
    # else:
    #     print('cron error account_balance')