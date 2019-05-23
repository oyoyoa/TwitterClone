import dj_database_url

from .base import *


DEBUG = False
SECRET_KEY = '@(o)5pq(3(fj#^s_n!vik&e0o@+6ezbjpbf^8(gst@(f+z(rjb'

DATABASES = {
    'default': dj_database_url.config()
}
ALLOWED_HOSTS = ['*']
