from django.conf.urls import patterns, include, url
from mystore import settings, views

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'mystore.views.index'),
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve',  
         {'document_root': settings.MEDIA_ROOT}),
    url(r'^products/$', views.all_products),
    url(r'^products/category/$', views.all_category),
    url(r'^products/category/(\w{1,10})/$', views.category_browse),
    url(r'^products/details/(\w{1,10})/$', views.product_detail),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
)
