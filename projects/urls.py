from django.conf.urls import patterns, url
from django.contrib import admin

from projects.views import (
    ProjectCreate,
    ProjectIndex,
    ProjectDetails,
    SyncWithTrello
)

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', ProjectIndex.as_view(), name='index'),
    url(r'^create/$', ProjectCreate.as_view(), name='create'),
    url(r'^details/(?P<id>\d+)/$', ProjectDetails.as_view(), name='details'),
    url(r'^sync/(?P<id>\d+)/$', SyncWithTrello.as_view(), name="sync")
)
