from django.conf.urls import patterns, include, url
from mystore import settings, views
from django.http import HttpResponseRedirect
from shop import urls as shop_urls

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', lambda x: HttpResponseRedirect('/shop/')),
	url(r'^shop/products/$', lambda x: HttpResponseRedirect('/shop/categories/')),
	url(r'^shop/categories/(?P<slug>[\w-]+)/$', 'products.views.category_detail'),
    url(r'^shop/categories/$', 'products.views.categories'),
	url(r'^shop/', include(shop_urls)),
	url(r'^search/$', 'products.views.search'),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root': settings.MEDIA_ROOT}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/profile/$', 'customers.views.profile'),
    url(r'^accounts/profile/edit$', 'customers.views.edit_profile'),
    url(r'^accounts/profile/form/phonenumber$', 'customers.views.change_number'),
    url(r'^accounts/profile/form/address$', 'customers.views.address_form'),
    url(r'^accounts/profile/form/address/(\w{1,2})$', 'customers.views.edit_address'),
    url(r'^accounts/profile/form/address/delete/(\w{1,2})$', 'customers.views.delete_address'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^contact/$', 'mystore.views.contact'),
    url(r'^contact/thanks/$', 'mystore.views.thanks'),
    url(r'^users/[\w-]+/$', lambda x: HttpResponseRedirect('/accounts/profile/')),
)
