from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'VideoMoodServer.views.home', name='home'),
    # url(r'^VideoMoodServer/', include('VideoMoodServer.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^VideoMoodApp/$', 'VideoMoodApp.views.search'),
    url(r'^VideoMoodApp/insert/$', 'VideoMoodApp.views.insert'),
    url(r'^VideoMoodApp/result/$', 'VideoMoodApp.views.result'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^VideoMoodApp/lookup/$', 'book_lookup'),
    url(r'^VideoMoodApp/insert_video/$', 'VideoMoodApp.views.insert'),
    url(r'^VideoMoodApp/base/$', 'VideoMoodApp.views.base')
)
