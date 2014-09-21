from django.conf.urls import patterns, include, url
from django.contrib import admin
from STManager.views import Home

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', Home.as_view(), name='home'),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^projects/', include('projects.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
