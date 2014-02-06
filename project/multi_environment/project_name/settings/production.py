# Production settings override.  Place any settings you wish to use in your production environment here.

from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

ROOT_URLCONF = '{{ project_name }}.urls.production'

WSGI_APPLICATION = '{{ project_name }}.wsgi.production.application'

# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'production.sqlite3'),
    }
}
