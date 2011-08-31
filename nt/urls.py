from django.conf.urls.defaults import *
from nt.nodetoys.views import NodeToy
from django.contrib import admin

#admin.autodiscover()

nt = NodeToy()

urlpatterns = patterns('',
    (r'^admin/?$',admin.site.root),
    (r'^request/echo/?$',nt.gview,{'view':'requestEcho'}),
)
