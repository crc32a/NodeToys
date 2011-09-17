from django.conf.urls.defaults import *
from nt.nodetoys.views import NodeToy
from django.contrib import admin

#admin.autodiscover()

nt = NodeToy()

urlpatterns = patterns('',
    (r'^request/echo/?$',nt.gview,{'view':'requestEcho'}),
    (r'^request/big/?$',nt.gview,{'view':'bigrequest'}),
    (r'^request/status/([0-9]+)/?$',nt.gview,{'view':'requestStatus'}),
    (r'^send/bytes/([0-9]+)$',nt.gview,{'view':'sendBytes'}),
    (r'^request/sleep/([0-9]+)$',nt.gview,{'view':'requestSleep'}),
    (r'^request/hello(/[0-9]+)?/?$',nt.gview,{'view':'requestHello'}),
    (r'^request/yhwh/?$',nt.gview,{'view':'requestYhwh'}),
    (r'^request/version/?$',nt.gview,{'view':'requestVersion'}),
)
