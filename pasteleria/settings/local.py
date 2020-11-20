from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'q+_6e6@iznrit+28!^r83zqb&1(vo64l)zbv)f#s$fwrn6!rn!'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
