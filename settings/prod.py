from .base import *
import os

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'xraennoq_esforcacarte',
        'USER' : 'xraennoq_esforcacarte',
        'PASSWORD' : 'Esforca@2025',
        'HOST' : "localhost",
        'PORT' : '3306',
    }
}