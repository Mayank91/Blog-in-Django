from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^home', 'myblog.views.home', name='home'),
    url(r'^post', 'myblog.views.post', name='post'),
    url(r'^contact', 'myblog.views.contact', name='post'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
