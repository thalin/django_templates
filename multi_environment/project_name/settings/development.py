# Development settings override.  Place any settings you wish to use in your development environment here.

from .base import *

INSTALLED_APPS += (
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls.development'
