from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Admin docs
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Admin app
    url(r'^admin/', include(admin.site.urls)),

    # Blog app
    url(r'^', include('blog.urls', namespace="blog")),
)

