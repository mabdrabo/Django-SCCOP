from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Django_SCCOP.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^about$', TemplateView.as_view(template_name='about.html'), name="about"),
	url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name="contact"),
)
 
urlpatterns += patterns('sccop.views',
	url(r'^$', "master", name="home"),
	url(r'^login$', "login", name="login"),
	url(r'^logout$', "logout", name="logout"),
	url(r'^email/send$', "email_send", name="email_send"),
	url(r'^dashboard$', "dashboard", name="dashboard"),
	url(r'^log$', "log", name="log"),
)

urlpatterns += patterns('sccop.api',
	url(r'^api/log/add/$', "add", name="api_add_log"),
)
