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

urlpatterns += patterns('gewb.views',
    url(r'^$', "master", name="home"),
    url(r'^signup$', "signup", name="signup"),
    url(r'^signin$', "signin", name="signin"),
    url(r'^signout$', "signout", name="signout"),
    url(r'^dashboard$', "dashboard", name="dashboard"),
    url(r'^relation/add/(?P<username>\w+)$', "add_track", name="add_track"),
    url(r'^relation/delete/(?P<username>\w+)$', "delete_track", name="delete_track"),
    url(r'^timeline/(?P<username>\w+)$', "viewLog", name="view_log"),
    url(r'^emergency/(?P<em_type>\w+)/add/$', "add_emergency", name="add_emergency"),
)

urlpatterns += patterns('sccop.views',
	url(r'^$', "master", name="home"),
	url(r'^signup$', "signup", name="signup"),
	url(r'^signin$', "signin", name="signin"),
	url(r'^signout$', "signout", name="signout"),
	url(r'^email/send$', "email_send", name="email_send"),
	# url(r'^dashboard$', "dashboard", name="dashboard"),
	# url(r'^log$', "log", name="log"),
	url(r'^sound/record$', "soundRecord", name="sound_record"),
)

urlpatterns += patterns('sccop.api',
	url(r'^api/update/state/$', "updateState", name="update_state"),
	url(r'^api/update/location/$', "updateLocation", name="update_location"),
)
