from django.conf.urls import patterns, include, url
from django.contrib import admin
from STManager.views import Home
from tasks.views import TasksIndex

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', TasksIndex.as_view())
)
