# Production settings override.  Place any settings you wish to use in your production environment here.

from .base import *

DEBUG = False

TEMPLATE_DEBUG = False

ROOT_URLCONF = '{{ project_name }}.urls.production'

WSGI_APPLICATION = '{{ project_name }}.wsgi.production.application'

# Define your production DATABASES setting here.
