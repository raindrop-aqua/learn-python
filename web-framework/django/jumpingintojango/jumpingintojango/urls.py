from django.conf.urls import patterns, include, url
from django.contrib import admin


urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'jumpingintojango.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),
                       url(r'^$', 'jumpingintojango.views.home', name='home'),
                       url(r'^login/$', 'jumpingintojango.views.login_view', name='login'),
                       url(r'^logout/$', 'jumpingintojango.views.logout_view', name='logout'),
                       url(r'^questions/$', 'questionsandanswers.views.index', name='index'),
                       url(r'^questions/(?P<question_id>\d+)', 'questionsandanswers.views.detail', name='detail'),
                       url(r'^questions/create/$', 'questionsandanswers.views.create', name='create'),
                       url(r'^questions/edit/(?P<question_id>\d+)', 'questionsandanswers.views.edit', name='edit'),
                       url(r'^admin/', include(admin.site.urls)),
)
