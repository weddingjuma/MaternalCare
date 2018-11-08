"""
Django settings for amama project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import django_heroku
import dj_database_url
from decouple import config, Csv
import django_pesapal

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'v%=2_05cj_kkr%!oosk*n$6f11pht(lc2bw06--%s0ntpxpx0u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []
# Application definition

INSTALLED_APPS = [
    'bootstrap4',
    'pesapal',
    'mama.apps.MamaConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_pesapal',
    'drift_chatwidget',

]

SITE_ID = 1

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'amama.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'amama.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Africa/Nairobi'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


# Media uploads path setting
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


DRIFT_CHAT_WIDGET = {
    'ID': '[khbmcsxs57yx]'
}
# ***************************************************
DISABLE_COLLECTSTATIC = config('DISABLE_COLLECTSTATIC')
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

django_heroku.settings(locals())

# *****************************************************

MODE = config("MODE", default="dev")
SECRET_KEY = 'v%=2_05cj_kkr%!oosk*n$6f11pht(lc2bw06--%s0ntpxpx0u'
DEBUG = config('DEBUG', default=True, cast=bool)
# development

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'amama',
        'USER': 'emdee',
        'PASSWORD': 'arif@123',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)
ALLOWED_HOSTS = ['amama.herokuapp.com', 'localhost', '127.0.0.1']

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"level": "DEBUG", "class": "logging.StreamHandler"}},
    "loggers": {
        "django_pesapal": {"handlers": ["console"], "level": "DEBUG", "propagate": True}
    },
}

PESAPAL_DEMO = True
PESAPAL_OAUTH_CALLBACK_URL = "transaction_completed"
PESAPAL_OAUTH_SIGNATURE_METHOD = "SignatureMethod_HMAC_SHA1"
PESAPAL_TRANSACTION_DEFAULT_REDIRECT_URL = 'home'
PESAPAL_TRANSACTION_FAILED_REDIRECT_URL = ""
PESAPAL_ITEM_DESCRIPTION = False
PESAPAL_TRANSACTION_MODEL = "pesapal.Transaction"
PESAPAL_CONSUMER_KEY = "qn8+6iz9KNHNiBmBrsB9OdnEhOWb1KlO"
PESAPAL_CONSUMER_SECRET = 'tvXP5OJCTpXYD6ZPeCmMnh/lqYc='
# Override pesapal keys
