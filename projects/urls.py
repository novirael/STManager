from django.conf.urls import patterns, url
from django.contrib import admin

from projects.views import AddProject, ProjectIndex, ProjectDetails


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', ProjectIndex.as_view(), name='index'),
    url(r'^add/$', AddProject.as_view(), name='add'),
    url(r'^(?P<id>\d+)/$', ProjectDetails.as_view(), name='details'),
)
