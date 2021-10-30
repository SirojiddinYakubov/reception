from io import BytesIO

import pyotp as pyotp
from PyPDF2 import PdfFileWriter, PdfFileReader
from django.http import HttpResponse
from django.template.loader import get_template
from rest_framework_simplejwt.tokens import RefreshToken
from xhtml2pdf import pisa

from reception.api import SendSmsWithApi
from reception.telegram_bot import send_message_to_developer


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def send_otp(phone):
    secret = pyotp.random_base32()
    totp = pyotp.TOTP(secret, interval=315360000)
    otp = totp.now()
    phone = str(phone)
    context = {
        'phone': phone,
        'secret': secret,
        'otp': otp
    }
    print(f"phone: {phone}, otp: {otp}")
    return context


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


# response = Response(serializer.data, status=201)
# url = request.build_absolute_uri(reverse('token_obtain_pair'))
# payload = {
#     'username': user.username,
#     'password': user.turbo,
# }
# r = requests.post(url, data=payload)
# try:
#     token = r.json()['access']
#     response.set_cookie(token, max_age=TOKEN_MAX_AGE)
# except:
#     send_message_to_developer(
#         f'Cookie set token error! Login: {user.username} Parol: {user.turbo}')
# return response
