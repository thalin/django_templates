from .base import *

from django.conf.urls import include, patterns, url

import debug_toolbar

urlpatterns += patterns('',
    url(r'__debug__/', include(debug_toolbar.urls)),
)
