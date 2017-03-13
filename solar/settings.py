"""
Django settings for solar project.

Generated by 'django-admin startproject' using Django 1.10.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""
import json
from pathlib import Path
import os

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).parents[2]  # project folder

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/


def get_secret(setting):
    file_path = str(BASE_DIR / 'solar' / 'solar' / 'settings_secrets.json')
    try:
        with open(file_path) as file:
            secrets = json.loads(file.read())
            try:
                return secrets[setting]
            except KeyError:
                error_message = "Set the {0} environment variable".format(setting)
                raise ImproperlyConfigured(error_message)
    except FileNotFoundError:
        error_message = "settings_secrets.json not found in settings folder"
        raise ImproperlyConfigured(error_message)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '#iif#6@kv$psf9(91b8lby#(@f1axd7$=9!fiz6afopc&sq^y&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'solartaskproject.herokuapp.com', 'localhost', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tracking',
    'grappelli',
    'django.contrib.admin',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'solar.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'solar.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd7s2uu51j56k1d',
        'USER': 'mpvrzeugsrmqjb',
        'PASSWORD': '32650dd659da2262260e30eafbd2c3c23af5afff38e04ae34781ecc07d06ea14',
        'HOST': 'ec2-54-163-236-33.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'solar_db',
#         'USER': 'OMAPALTECHNOLOGIES',
#         'PASSWORD': 'admin123',
#         'HOST': '127.0.0.1',
#         'PORT': '5432',
#     }
# }

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = "eynimumbaiindia@gmail.com",
EMAIL_HOST_PASSWORD = "liomessi10"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# SERVER_EMAIL = "mushahidk545@gmail.com"

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/
# STATIC_ROOT = str(BASE_DIR  / 'solar'/ 'solar' /'static')
# STATIC_URL = '/static/'
# STATICFILES_DIRS = (
#     str(BASE_DIR / "/solar" / " solar" / "static"),
#     # '/var/www/static/',
# )
# STATIC_ROOT = str(BASE_DIR / 'solar' / 'staticfiles')
GRAPPELLI_ADMIN_TITLE = "OORJAN BACKEND ADMIN"

STATIC_ROOT = str(BASE_DIR / 'solar' / 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
