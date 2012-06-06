from django.conf.urls import patterns, include, url
from softball.views import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', stat_table_spring),
    # Examples:
    # url(r'^$', 'fifth_base.views.home', name='home'),
    # url(r'^fifth_base/', include('fifth_base.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
