from django.conf.urls import patterns, url
from django.contrib import admin
from projects.views import ProjectView, AddProject


admin.autodiscover()
urlpatterns = patterns(
    '',
    url(r'^$', ProjectView.as_view()),
    url(r'^add/$', AddProject.as_view()),
    # url(r'^(?P<id>\d+)/start/$', StartTask.as_view()),
    # url(r'^(?P<id>\d+)/stop/$', StopTask.as_view()),
)
