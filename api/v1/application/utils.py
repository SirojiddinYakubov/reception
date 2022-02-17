from rest_framework.views import APIView

from reception.api import SendSmsWithPlayMobile, SUCCESS, SendSmsWithApi
from reception.telegram_bot import send_message_to_developer
from user.models import User, CHECKER


class ApplicationSuccessCreatedMessage:
    def __init__(self, application):
        self.application = application

    def get(self):
        help_text = f"Arizangiz {self.application.section.title}ga  jo'natildi. To'lov qilish va keyingi bosqich bo'yicha savollaringiz bo'lsa 972800809 raqamiga qo'ng'iroq qiling"
        applicant_phone = self.application.applicant.phone if self.application.applicant else self.application.created_user.phone
        r = SendSmsWithPlayMobile(phone=applicant_phone, message=help_text).get()
        # r = 200
        if not r == SUCCESS:
            r = SendSmsWithApi(message=help_text, phone=applicant_phone).get()
            if not r == SUCCESS:
                send_message_to_developer('Sms service not working!')

        text = f"E-RIB.UZ Onlayn ariza platformasiga {self.application.id}-raqamli ariza kelib tushdi. \nIltimos arizani ko'rib chiqish uchun qabul qiling. Fuqaro sizning javobingizni kutmoqda! {'Avtomobil:' + self.application.car.old_number if self.application.car.old_number else ''}"
        inspectors = User.objects.filter(section=self.application.section, role__in=[CHECKER])

        if inspectors:
            for inspector in inspectors:
                r = SendSmsWithPlayMobile(phone=inspector.phone, message=text).get()
                # r = 200
                if not r == SUCCESS:
                    r = SendSmsWithApi(message=text, phone=inspector.phone).get()
                    if not r == SUCCESS:
                        send_message_to_developer('Sms service not working!')
        return 200

