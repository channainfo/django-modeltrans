"""
Django settings for migrate_test project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import sys

from django.utils.translation import ugettext_lazy as _

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "_84!q(@lf&lovmoj55#(!pw^r!(3ss*-lj7+w5#)f%3j4geg-i"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "modeltranslation",
    # "modeltrans",
    "migrate_test.app",
]

ROOT_URLCONF = "migrate_test.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "migrate_test.wsgi.application"


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "modeltrans-migration",
        "USER": "postgres",
        "PASSWORD": "test1234",
        "HOST": "localhost",
        "PORT": 5432,
        "CONN_MAX_AGE": 600,
        "TEST": {"NAME": "modeltrans-migration"},
    }
}
if "TRAVIS" in os.environ:
    DATABASES["default"].update(
        {
            "NAME": "modeltrans-migration",
            "TEST": {"NAME": "modeltrans-migration"},
            "USER": "postgres",
            "PASSWORD": "",
            "HOST": "localhost",
            "PORT": "",
        }
    )

# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en-us"

LANGUAGES = [("de", _("German")), ("en", _("English")), ("nl", _("Dutch")), ("fr", _("French"))]

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = "/static/"

if "test" in sys.argv:
    print("\n\033[33mWarning\033[00m: Running without migrations")

    class DisableMigrations(object):
        def __contains__(self, item):
            return True

        def __getitem__(self, item):
            return None

    MIGRATION_MODULES = DisableMigrations()
