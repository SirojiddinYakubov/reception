from io import BytesIO

import pyotp as pyotp
from PyPDF2 import PdfFileWriter, PdfFileReader
from django.http import HttpResponse
from django.template.loader import get_template
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
