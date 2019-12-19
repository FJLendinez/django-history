# -*- coding: utf-8
import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "##################################################"

DATABASES = {
    "default": {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': 'debug',
        'PASSWORD': 'debug',
        'HOST': '127.0.0.1',
        'PORT': '5200',
        'NAME': "postgres",
        'TEST': {
            'NAME': 'mytestdatabase',
        },
    }
}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "django_history",
    "tests.fake_models"
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()
