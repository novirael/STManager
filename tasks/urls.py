from django.conf.urls import patterns, url
from django.contrib import admin

from tasks.views import TasksIndex, AddTask


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TasksIndex.as_view(), name="index"),
    url(r'^add/$', AddTask.as_view(), name="add"),
)
