from .base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql', # Conector de DB
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': 'cuperx',
        'HOST': 'localhost',
        'PORT': '5432'
    }
}