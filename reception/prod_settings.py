import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import sys

from loguru import logger

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x9fq&#!x9v_%^&^*(&*)%$&^%%&^8976jo@-_oq5nvqc($wlbq23)'

from dotenv import load_dotenv

env_path = "./deploy/.env"
load_dotenv(dotenv_path=env_path)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['e-rib.uz', 'www.e-rib.uz', '89.108.77.160']

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": os.getenv("DB_NAME"),
        "USER": os.getenv("DB_USER"),
        "HOST": os.getenv("DB_HOST"),
        "PORT": os.getenv("DB_PORT"),
        "PASSWORD": os.getenv("DB_PASSWORD"),
    }
}

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'static')
# ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOG_FILE_PATH = '/home/pyth/reception/logs/debug.log'
logger.add(sys.stderr, format="{time} {level} {messege}", level="DEBUG")
# logger.debug('DEBUG')
# logger.info('INFO')
# logger.error('ERROR')
