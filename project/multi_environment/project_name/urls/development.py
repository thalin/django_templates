from .base import *

import debug_toolbar

urlpatterns += patterns('',
    url(r'__debug__/', include(debug_toolbar.urls)),
)
