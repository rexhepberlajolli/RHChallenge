from .base import *

ALLOWED_HOSTS = ['*']


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '5n$pp1rl5xqvf7=!4ikzfob9b=)j%78df9bnkawz84wsl-z48z'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'RH_CH_DB',
        'USER': 'RHCH',
        'PASSWORD': '42d31ae0c55d494b8861be0e6',
        'HOST': 'db',
        'PORT': 5432,
    }
}


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '[%(levelname)s] [%(asctime)s] [%(module)s] %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        '': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
        'django.request': {
            'handlers': ['console'],
            'propagate': False,
            'level': 'DEBUG'
        }
    }
}


# Google O Auth KEYS

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '643543659972-76ru1rbm452h1028j2lndr3ua7b4amhq.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'i9-lKPxAox6i-iXlMpPKm8HJ'
