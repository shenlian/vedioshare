from django.conf.urls import patterns, include, url
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
import settings

admin.autodiscover()
dajaxice_autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$','home.views.index'),
    # url(r'^vedioshare/', include('vedioshare.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^normal/', include('normal.urls')),
    url(r'^registration/',include('registration.urls'),),
    url(dajaxice_config.dajaxice_url,include('dajaxice.urls')),
	url(r'^replay/(?P<pid>.{36})$','normal.views.replay',name = "replay"),
)
# for develop to serve user-upload content in MEDIA_ROOT
if settings.DEBUG:
	 urlpatterns += patterns('',
			 url(r'^media/(?P<path>.*)$',
				 'django.views.static.serve',
				 {'document_root': settings.MEDIA_ROOT}),
				 )



