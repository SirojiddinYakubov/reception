import json
import os
import random
import time
from types import FunctionType
import requests
from django.core.exceptions import ValidationError
from django.http import HttpResponse, JsonResponse
from requests.auth import HTTPBasicAuth

from reception.telegram_bot import send_message_to_developer
from service.models import PaymentForTreasury

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
        try:
            data = {
                'email': os.getenv('SMS_BROKER_EMAIL'),
                'password': os.getenv('SMS_BROKER_PASSWORD'),
            }

            AUTHORIZATION_URL = 'http://notify.eskiz.uz/api/auth/login'

            r = requests.request('POST', AUTHORIZATION_URL, data=data)
            if r.json()['data']['token']:
                return r.json()['data']['token']
            else:
                return FAILED
        except Exception as e:
            print('SMS_BROKER_EMAIL and SMS_BROKER_PASSWORD not found')
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


class SendSmsWithPlayMobile:
    def __init__(self, phone, message=None):
        self.phone = phone
        self.message = message
        self.spend = None
        self.message_id = random.randint(100000000, 999999999)
        self.username = os.getenv('PLAY_MOBILE_USERNAME')
        self.password = os.getenv('PLAY_MOBILE_PASSWORD')

    def get(self):
        step1 = self.custom_validation()
        if step1 == SUCCESS:
            message = self.clean_message(self.message)
            step3 = self.calculation_send_sms(message)
            if step3 == SUCCESS:
                return self.send_message(message)

    def custom_validation(self):
        if not len(str(self.phone)) == 9:
            return INVALID_NUMBER
        if self.message == '' or self.message == None:
            return MESSAGE_IS_EMPTY
        return SUCCESS

    def send_message(self, message):
        try:
            URL = os.getenv('PLAY_MOBILE_URL')
            headers = {'Content-type': 'application/json'}
            payload = {
                "messages": [
                    {
                        "recipient": "998" + str(self.phone),
                        "message-id": "1234564566",
                        "sms": {
                            "originator": "3700",
                            "content": {
                                "text": str(message),
                            }
                        }
                    }
                ]
            }

            r = requests.post(URL, json=payload, headers=headers,
                              auth=(self.username, self.password))

            if not r.status_code == SUCCESS:
                send_message_to_developer('Send sms error with play mobile')

            try:
                from user.models import Sms
                Sms.objects.create(sms_id=self.message_id, sms_count=self.spend, text=str(message),
                                   phone=self.phone, is_playmobile=True)
            except:
                send_message_to_developer("sms object create error: api.py line:256")

            return SUCCESS
        except Exception as e:
            print(e)
            send_message_to_developer(f"sms object create error: {e}")
            return FAILED

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


class PaymentByRequisites:
    """https://noon-warbler-f6e.notion.site/10f6bb76a73949fa990b44965a4d8851"""

    def __init__(self):
        self.username = os.getenv('APELSIN_USERNAME')
        self.password = os.getenv('APELSIN_PASSWORD')
        self.merchant_id = 998747
        self.url = "https://topup.apelsin.uz/api/merchant/"
        self.headers = {'Content-type': 'application/json'}
        self.token = None
        self.phone = None
        self._id = None

    def get_pay_from_card(self, card_number, exp_date, amount):
        get_phone = self.cards_get_phone(card_number, exp_date)
        if get_phone['status'] == SUCCESS:
            create_amount = self.create_amount(amount)
            if create_amount['status'] == SUCCESS:
                confirm_pay = self.confirm_pay(self._id, self.token)
                if confirm_pay['status'] == SUCCESS:
                    return {'status': SUCCESS, 'result': confirm_pay['result']}
                else:
                    return {'status': FAILED, 'result': confirm_pay['result']}
            else:
                return {'status': FAILED, 'result': create_amount['result']}
        else:
            return {'status': FAILED, 'result': get_phone['result']}

    def cards_get_phone(self, card_number, exp_date):
        get_phone_payload = json.dumps({
            "method": "cards.get_phone",
            "params": {
                "number": card_number,
                "expire": exp_date
            },
            "id": 0
        })
        get_phone = requests.request("POST", url=self.url, data=get_phone_payload, headers=self.headers,
                                     auth=(self.username, self.password))

        """
        success:
        {
            "error": null,
            "result": {
                "card": {
                    "token": "N+qQnaWR9J9PGwr/4hIZz5aZeVlLgtODSk7OBlgva1k=",
                    "phone": "998919791999"
                }
            },
            "id": 0
        }
        error:
        {
            "error": "Cannot determine centre and prefix for card 986006******1059",
            "result": null,
            "id": 0
        }
        """

        try:
            print(get_phone.json(), 392)
            if isinstance(get_phone.json()['result'], dict):
                self.token = get_phone.json()['result']['card']['token']
                self.phone = get_phone.json()['result']['card']['phone']
                return {'status': SUCCESS, 'result': None}
            else:
                return {'status': FAILED, 'result': "Karta raqami yoki amal qilish muddati noto'g'ri!"}
        except Exception as e:
            print(e, 400)
            return {'status': FAILED, 'result': get_phone.json()}

    def create_amount(self, amount):
        create_amount_payload = json.dumps({
            "method": "receipt.create",
            "params": {
                "merchant_id": self.merchant_id,
                "amount": amount,
                "account": [
                    {
                        "field": "test",
                        "value": "test"
                    }
                ],
                "lang": "ru"
            }, "id": 0
        })

        create_amount = requests.request("POST", url=self.url, data=create_amount_payload, headers=self.headers,
                                         auth=(self.username, self.password))

        """
        success:
        {
            "error": null,
            "result": {
                "receipt": {
                    "_id": "a110fa3afede4ffcbf8b075495eb39cd",
                    "state": 0,
                    "create_date": 1638680553820,
                    "pay_date": 0,
                    "error": null,
                    "type": 1,
                    "card": null,
                    "merchant": {
                        "_id": "998747",
                        "name": "Open Soft",
                        "organization": "Прямой договор",
                        "logo": null
                    },
                    "description": "",
                    "account": [
                        {
                            "name": "test",
                            "value": "test"
                        }
                    ],
                    "detail": null,
                    "amount": 100000,
                    "currency": 0,
                    "commission": 0
                }
            },
            "id": 0
        }
        error:
        {
            "error": "Merchant not found",
            "result": null,
            "id": 0
        }
        """

        try:
            print(create_amount.json())
            if isinstance(create_amount.json()['result'], dict):
                self._id = create_amount.json()['result']['receipt']['_id']
                return {'status': SUCCESS, 'result': None}
            else:
                send_message_to_developer(f"error: {create_amount.json()}")
                return {'status': FAILED,
                        'result': "Xatolik! Profilaktika ishlari olib borilmoqda! Iltimos keyinroq urinib ko'ring!"}
        except Exception as e:
            print(e)
            send_message_to_developer(f"error: {e}")
            return {'status': FAILED,
                    'result': "Xatolik! Profilaktika ishlari olib borilmoqda! Iltimos keyinroq urinib ko'ring!"}

    def confirm_pay(self, _id, token):
        confirm_pay_payload = json.dumps({
            "method": "receipt.pay_by_card",
            "params": {
                "id": _id,
                "card": {
                    "token": token
                },
                "lang": "uz"
            }
        })
        confirm_amount = requests.request("POST", url=self.url, data=confirm_pay_payload, headers=self.headers,
                                          auth=(self.username, self.password))

        """
        success:
        {
            "error": null,
            "result": {
                "receipt": {
                    "_id": "8ac55f5eed7a4b2d908880be02afaf2d",
                    "state": 4,
                    "create_date": 1638697387049,
                    "pay_date": 1638697474776,
                    "error": null,
                    "type": 1,
                    "card": {
                        "token": "vzdu2GZqvX3iSI4CxBV883UAE1kenoVephsLa1xxT1s="
                    },
                    "merchant": {
                        "_id": "998747",
                        "name": "Open Soft",
                        "organization": "Прямой договор",
                        "logo": null
                    },
                    "description": null,
                    "account": null,
                    "detail": null,
                    "amount": 100000,
                    "currency": 860,
                    "commission": 0
                }
            },
            "id": 0
        }
        error:
        {
            "error": "Receipt can not pay",
            "result": null,
            "id": 0
        }
        """

        try:
            print(confirm_amount.json())
            if confirm_amount.json()['result']['receipt']['state'] == 4:
                return {'status': SUCCESS,
                        'result': confirm_amount.json()['result']['receipt']['_id']}
            elif confirm_amount.json()['result']['receipt']['error'] == 'Insufficient funds':
                return {'status': FAILED,
                        'result': "Xatolik! Kartangizda yetarli mablag' mavjud emas!"}
            else:
                return {'status': FAILED,
                        'result': "Xatolik! Profilaktika ishlari olib borilmoqda! Iltimos keyinroq urinib ko'ring!"}
        except Exception as e:
            send_message_to_developer(f"error: {e}")
            print(e)
            return {'status': FAILED,
                    'result': "Xatolik! Profilaktika ishlari olib borilmoqda! Iltimos keyinroq urinib ko'ring!"}

    def get_card_phone_number(self, card_number, exp_date):
        get_phone_payload = json.dumps({
            "method": "cards.get_phone",
            "params": {
                "number": card_number,
                "expire": exp_date
            },
            "id": 0
        })
        get_phone_number = requests.request("POST", url=self.url, data=get_phone_payload, headers=self.headers,
                                            auth=(self.username, self.password))

        try:
            print(get_phone_number.json())
            if 'status' in get_phone_number.json():
                if get_phone_number.json()['status'] == 'UNAUTHORIZED':
                    return {'status': FAILED, 'result': "Xatolik! Avtorizatsiya amalga oshmadi!"}

            if isinstance(get_phone_number.json()['result'], dict):
                phone = get_phone_number.json()['result']['card']['phone']
                if len(phone) == 12:
                    return {'status': SUCCESS, 'result': phone[3:12]}
                else:
                    return {'status': FAILED, 'result': "Ushbu kartada sms xizmati yoqilmagan!"}
            else:
                send_message_to_developer(f"error: {json.dumps(get_phone_number.json())}")
                return {'status': FAILED, 'result': "Karta raqami yoki amal qilish muddati noto'g'ri!"}
        except:
            return {'status': FAILED, 'result': "Xatolik! Sahifani yangilab qayta urinib ko'ring!"}

    def pay_treasury(self, pay, payload):
        pay_treasury = requests.request("POST", url="https://topup.apelsin.uz/api/merchant/", data=payload,
                                        headers={'Content-type': 'application/json'},
                                        auth=(os.getenv('APELSIN_USERNAME'), os.getenv('APELSIN_PASSWORD')))

        """
        success:
        {'receipt': 
            {
            '_id': '8be8b1cff59d4281888ba2825a0d3967', 
            'state': 30, 
            'create_date': 1638719484991, 
            'pay_date': 1638719486245, 
            'error': None, 'type': 7, 
            'card': {'sender_id': '29896000705447577002'}, 
            'merchant': None, 
            'description': None, 
            'account': None, 
            'detail': 
                {   
                    "account": "20208000305447577001",
                    "mfo":"00966",
                    "name": "hjghj1 hjghjg1 ghjghj1",
                    "details":"Qayta ro\'yhatlash uchun to\'lov (E-RIB.UZ 308944250)",
                    "senderName":"OOO OPENSOFT",
                    "memorial":"https://ek.apelsin.uz/memorial?id=RX%2Bq4L%2FXxo2kOc6%2FUgUQ5jXNmoNfGxXLpyLe%2BSE3Zc4PI0FpRjY33bdMH8BX%2FevW",
                    "externalTransactionId":"1638719626"
                }', 
            'amount': 101000, 
            'currency': 860, 
            'commission': 1000
            }
        }
        """

        try:
            if 'error' in pay_treasury.json():
                if pay_treasury.json()['error'] == 'External id exists':
                    return {'status': FAILED, 'result': "Xatolik! Bunday ID raqamli to'lov avval amalga oshirilgan!"}
            else:
                print(pay_treasury.json())
                if pay_treasury.json()['receipt']['state'] == 30:
                    memorial = json.loads(pay_treasury.json()['receipt']['detail'])
                    memorial = memorial['memorial']
                    memorial = memorial.replace("memorial", 'pdf')

                    return {'status': SUCCESS,
                            'result': {'memorial': memorial, '_id': pay_treasury.json()['receipt']['_id']}}

        except Exception as e:
            send_message_to_developer(f"error: {e}")
            return {'status': FAILED, 'result': "Xatolik!"}
