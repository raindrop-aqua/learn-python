from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'simpleblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'', 'blog.views.main'),
    url(r'^(\d+)/$', 'post'),
    url(r'^add_comment/(\d+)/$', 'add_comment'),
)
