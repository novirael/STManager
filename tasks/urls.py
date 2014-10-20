from django.conf.urls import patterns, url
from django.contrib import admin

from tasks.views import (
    TasksIndex,
    AddTask,
    StartTask,
    StopTask,
    TaskDetails
)


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TasksIndex.as_view(), name="index"),
    url(r'^add/$', AddTask.as_view(), name="add"),
    url(r'^(?P<id>\d+)/start/$', StartTask.as_view(), name="start"),
    url(r'^(?P<id>\d+)/stop/$', StopTask.as_view(), name="stop"),
    url(r'^(?P<id>\d+)/$', TaskDetails.as_view(), name="details")
)
