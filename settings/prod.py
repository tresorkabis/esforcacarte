from .base import *
import dj_database_url
import os

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