from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'mysite.plots.views.index', name='index'),
#    url(r'^plots/', include('plots.urls')),
    url(r'^analyse/', 'mysite.plots.views.analyse', name='analyse'),
    url(r'^admin/', include(admin.site.urls)),
)
