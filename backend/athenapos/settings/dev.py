from .base import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'athenapos_db',
        'USER': 'athenapos_db',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}