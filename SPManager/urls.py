from django.conf.urls import patterns, include, url
from django.contrib import admin

from SPManager.views import Home


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^projects-manager/', include('projects_manager.urls', namespace='projects_manager')),
    url(r'^admin/', include(admin.site.urls)),
)
