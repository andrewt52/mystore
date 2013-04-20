from django.conf.urls import patterns, include, url
from mystore import settings, views
from django.http import HttpResponseRedirect
from shop import urls as shop_urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', lambda x: HttpResponseRedirect('/shop/')),
	url(r'^shop/', include(shop_urls)),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
