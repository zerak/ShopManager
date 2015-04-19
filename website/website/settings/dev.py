from .base import *

DEBUG = True
TEMPLATE_DEBUG = True

APPS = (
    # 'django_extensions',
)

INSTALLED_APPS += APPS

INTERNAL_IPS = ('127.0.0.1',)

DATABASES = {
     'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'django', 
        'USER': 'root',
        'PASSWORD': 'z456+987',
        'HOST': '',
        'PORT': '3306', 
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'