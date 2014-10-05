from django.conf.urls import patterns, include, url
from django.contrib import admin

from STManager.views import Home


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^tasks/', include('tasks.urls', namespace="tasks_app")),
    url(r'^projects/', include('projects.urls', namespace="projects_app")),
    url(r'^admin/', include(admin.site.urls)),
)
