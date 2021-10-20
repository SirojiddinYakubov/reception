from django.contrib.auth import get_user_model, authenticate
from rest_framework.authentication import get_authorization_header
from rest_framework import HTTP_HEADER_ENCODING
import base64
import binascii
from django.conf import settings
from reception.telegram_bot import send_message_to_developer

def authentication(request):
    """
           Returns a `User` if a correct username and password have been supplied
           using HTTP Basic authentication.  Otherwise returns `None`.
           """
    auth = get_authorization_header(request).split()
    send_message_to_developer(f"{request.POST} 15")
    if not auth or auth[0].lower() != b'basic':
        return False

    if len(auth) == 1:
        return False
    elif len(auth) > 2:
        return False

    try:
        auth_parts = base64.b64decode(auth[1]).decode(HTTP_HEADER_ENCODING).partition(':')
    except (TypeError, UnicodeDecodeError, binascii.Error):
        return False

    userid, password = auth_parts[0], auth_parts[2]
    return authenticate_credentials(userid, password, request)


def authenticate_credentials(userid, password, request=None):
    """
    Authenticate the userid and password against username and password
    with optional request for context.
    """
    key = settings.PAYCOM_SETTINGS['SECRET_KEY']
    send_message_to_developer(f"{key} 39")
    send_message_to_developer(f"{password} 40")
    send_message_to_developer(f"{userid} 41")
    if userid == 'Paycom' and password == key:
        return True
    return False
