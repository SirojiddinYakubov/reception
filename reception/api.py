import json
import time
from types import FunctionType
import requests
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse

from reception.telegram_bot import send_message_to_developer

SUCCESS = 200
PROCESSING = 102
FAILED = 400
INVALID_NUMBER = 160
MESSAGE_IS_EMPTY = 170
SMS_NOT_FOUND = 404
SMS_SERVICE_NOT_TURNED = 600

class SendSmsWithApi:
    def __init__(self, phone, message=None):
        self.phone = phone
        self.message = message
        self.spend = None

    def get(self):
        status_code = self.custom_validation()
        if status_code == SUCCESS:
            message = self.clean_message(self.message)
            spent = self.calculation_send_sms(message)
            if spent == SUCCESS:
                return self.send_message(message)
            return spent
        return status_code

    def custom_validation(self):
        if not len(str(self.phone)) == 9:
            return INVALID_NUMBER

        if self.message == '' or self.message == None:
            return MESSAGE_IS_EMPTY

        return SUCCESS

    def authorization(self):
        data = {
            'email': 'bcloudintelekt@gmail.com',
            'password': 'ddMFQPXTfQRuhj8nmNSyfLv6mniuSpBHxGj3ZEY5',
        }

        AUTHORIZATION_URL = 'http://notify.eskiz.uz/api/auth/login'

        r = requests.request('POST', AUTHORIZATION_URL, data=data)
        if r.json()['data']['token']:
            return r.json()['data']['token']
        else:
            return FAILED

    def send_message(self, message):
        token = self.authorization()
        # print(f"Token: {token}")
        if token == FAILED:
            return FAILED

        SEND_SMS_URL = "http://notify.eskiz.uz/api/message/sms/send"
        # STATUS_SMS_URL = "http://notify.eskiz.uz/api/message/sms/status/"

        PAYLOAD = {
            'mobile_phone': '998' + str(self.phone),
            'message': message,
            'from': '4546',
            'callback_url': 'http://afbaf9e5a0a6.ngrok.io/sms-api-result/'}

        FILES = [

        ]
        HEADERS = {
            'Authorization': f'Bearer {token}'
        }
        # print(f'message: {self.message}')
        r = requests.request("POST", SEND_SMS_URL, headers=HEADERS, data=PAYLOAD, files=FILES)
        print(r.json())
        try:
            from user.models import Sms
            Sms.objects.create(sms_id=r.json()['id'], sms_count=self.spend, text=self.message,
                               phone=self.phone)
        except:
            send_message_to_developer("sms object create error")
        return r.status_code
        # return SUCCESS

    def clean_message(self, message):
        message = message.replace('ц', 'ts').replace('ч', 'ch').replace('ю',
                                                                        'yu').replace(
            'а', 'a').replace('б', 'b').replace('қ', "q").replace('ў', "o'").replace('ғ', "g'").replace('ҳ',
                                                                                                        "h").replace(
            'х',
            "x").replace(
            'в', 'v').replace('г', 'g').replace('д', 'd').replace('е',
                                                                  'e').replace(
            'ё', 'yo').replace('ж', 'j').replace('з', 'z').replace('и', 'i').replace('й', 'y').replace('к',
                                                                                                       'k').replace(
            'л', 'l').replace('м', 'm').replace('н', 'n').replace('о', 'o').replace('п', 'p').replace('р',
                                                                                                      'r').replace(
            'с', 's').replace('т', 't').replace('у', 'u').replace('ш', 'sh').replace('щ', 'sh').replace('ф',
                                                                                                        'f').replace(
            'э', 'e').replace('ы', 'i').replace('я', 'ya').replace('ў', "o'").replace('ь', "'").replace('ъ',
                                                                                                        "'").replace(
            '’', "'").replace('“', '"').replace('”', '"').replace(',', ',').replace('.', '.').replace(':', ':')
        # filter upper
        message = message.replace('Ц', 'Ts').replace('Ч', 'Ch').replace('Ю', 'Yu').replace(
            'А', 'A').replace('Б', 'B').replace('Қ', "Q").replace('Ғ', "G'").replace('Ҳ', "H").replace('Х',
                                                                                                       "X").replace(
            'В', 'V').replace('Г', 'G').replace('Д', 'D').replace('Е',
                                                                  'E').replace(
            'Ё', 'Yo').replace('Ж', 'J').replace('З', 'Z').replace('И', 'I').replace('Й', 'Y').replace('К',
                                                                                                       'K').replace(
            'Л', 'L').replace('М', 'M').replace('Н', 'N').replace('О', 'O').replace('П', 'P').replace('Р',
                                                                                                      'R').replace(
            'С', 'S').replace('Т', 'T').replace('У', 'U').replace('Ш', 'Sh').replace('Щ', 'Sh').replace('Ф',
                                                                                                        'F').replace(
            'Э', 'E').replace('Я', 'Ya')
        return message

    def calculation_send_sms(self, message):
        try:
            length = len(message)
            if length:
                if length >= 0 and length <= 160:
                    self.spend = 1
                elif length > 160 and length <= 306:
                    self.spend = 2
                elif length > 306 and length <= 459:
                    self.spend = 3
                elif length > 459 and length <= 612:
                    self.spend = 4
                elif length > 612 and length <= 765:
                    self.spend = 5
                elif length > 765 and length <= 918:
                    self.spend = 6
                elif length > 918 and length <= 1071:
                    self.spend = 7
                elif length > 1071 and length <= 1224:
                    self.spend = 8
                else:
                    self.spend = 30
                return SUCCESS
            else:
                return MESSAGE_IS_EMPTY
        except:
            return FAILED


def sms_api_result(request):
    try:
        send_message_to_developer(f"{request}")
    except:
        if request:
            send_message_to_developer('sms from SmsApi, Eskiz.uz send sms')


# class GetStatusSms:
#     def __init__(self, id):
#         self.id = id
#
#     def authorization(self):
#         data = {
#             'email': 'bcloudintelekt@gmail.com',
#             'password': 'ddMFQPXTfQRuhj8nmNSyfLv6mniuSpBHxGj3ZEY5',
#         }
#
#         AUTHORIZATION_URL = 'http://notify.eskiz.uz/api/auth/login'
#
#         r = requests.request('POST', AUTHORIZATION_URL, data=data)
#         if r.json()['data']['token']:
#             return r.json()['data']['token']
#         else:
#             return FAILED
#
#     def get(self):
#
#         token = self.authorization()
#
#         CHECK_STATUS_URL = 'http://notify.eskiz.uz/api/message/sms/status/' + str(self.id)
#
#         HEADERS = {
#             'Authorization': f'Bearer {token}'
#         }
#
#         r = requests.request("GET", CHECK_STATUS_URL, headers=HEADERS)
#         if r.json()['status'] == 'success':
#             if r.json()['message']['status'] == 'DELIVRD' or r.json()['message']['status'] == 'TRANSMTD':
#                 return SUCCESS
#             elif r.json()['message']['status'] == 'EXPIRED':
#                 return FAILED
#             else:
#                 return PROCESSING
