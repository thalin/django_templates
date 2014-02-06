# Staging settings override.  Place any settings you wish to use in your staging environment here.

from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

ROOT_URLCONF = '{{ project_name }}.urls.production'

WSGI_APPLICATION = '{{ project_name }}.wsgi.staging.application'

# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'staging.sqlite3'),
    }
}
