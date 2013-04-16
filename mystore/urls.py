from django.conf.urls import patterns, include, url
from mystore import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'mystore.views.index'),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
