# Development settings override.  Place any settings you wish to use in your development environment here.

from .base import *

DEBUG = True

TEMPLATE_DEBUG = True

INTERNAL_IPS = [
    '127.0.0.1',
    '::1'
]

INSTALLED_APPS += (
    'debug_toolbar.apps.DebugToolbarConfig',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls.development'

WSGI_APPLICATION = '{{ project_name }}.wsgi.development.application'

# Database
# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'development.sqlite3'),
    }
}

# django-debug-toolbar settings
# https://django-debug-toolbar.readthedocs.org/en/latest/
DEBUG_TOOLBAR_PATCH_SETTINGS = False
