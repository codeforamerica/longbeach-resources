import dj_database_url
import os
from longbeach_resources.settings.base import *

SECRET_KEY = os.environ['DJANGO_SECRET_KEY']

ALLOWED_HOSTS = ['*']

DATABASES = {'default': dj_database_url.config(conn_max_age=600)}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

STATIC_ROOT = os.path.join(PROJECT_ROOT, '../staticfiles')

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

DEBUG = True
