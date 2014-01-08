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
)

urlpatterns += patterns('sccop.mobile',
	url(r'^mobile/update/$', "master", name="home"),
)
