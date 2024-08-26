from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-fp-5an!%l^myrj^9wmt+yp&pep@h-f*@$*x8wj@__emx8v3m-k'


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "cardatabase",
        "USER": "root",
        "PASSWORD": "",
        "HOST": "localhost",
    }
}