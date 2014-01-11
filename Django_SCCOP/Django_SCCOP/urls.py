from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_SCCOP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

)
 
urlpatterns += patterns('sccop.views',
	url(r'^$', "master", name="home"),
	url(r'^dashboard/(?P<username>\d+)$', "dashboard", name="dashboard"),
)

urlpatterns += patterns('sccop.api',
	url(r'^api/log/add/$', "add", name="api_add_log"),
)
