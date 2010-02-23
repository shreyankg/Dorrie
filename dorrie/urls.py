# Dorrie - Web interface for building Fedora Spins/Remixes. 
# Copyright (C) 2009 Red Hat Inc.
# Author: Shreyank Gupta <sgupta@redhat.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from django.conf import settings
from django.conf.urls.defaults import *
from comps import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^dorrie/', include('dorrie.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^$', views.home),
    (r'^basic/$', views.basic),
    (r'^packages/$', views.packages),
    (r'^select/$', views.select),
    (r'^build/$', views.build),
    (r'^process/$', views.process),
    (r'^tail/$', views.tail),
    # Uncomment the next line to enable the admin:
    # (r'^admin/(.*)', admin.site.root),
)

if settings.STATIC_SERVE:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$',
         'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    )

