from django.conf.urls import patterns, include, url
from mystore import settings, views
from django.http import HttpResponseRedirect
from shop import urls as shop_urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', lambda x: HttpResponseRedirect('/shop/')),
	url(r'^shop/categories/(?P<slug>[\w-]+)/$', 'products.views.category_detail'),
    url(r'^shop/categories/$', 'products.views.categories'),
	url(r'^shop/', include(shop_urls)),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/profile/$', 'mystore.views.profile'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^users/[\w-]+/$', lambda x: HttpResponseRedirect('/accounts/profile/')),
)
