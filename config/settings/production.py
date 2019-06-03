import dj_database_url
import django_heroku

from .base import *


DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}
ALLOWED_HOSTS = ['*']

django_heroku.settings(locals())
