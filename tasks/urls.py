from django.conf.urls import patterns, include, url
from django.contrib import admin
from STManager.views import Home
from tasks.views import TasksIndex, AddTask, StartTask, StopTask

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TasksIndex.as_view()),
    url(r'^add/$', AddTask.as_view()),
    url(r'^(?P<id>\d+)/start/$', StartTask.as_view()),
    url(r'^(?P<id>\d+)/stop/$', StopTask.as_view()),
)

