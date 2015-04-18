from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf import settings
from . import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$',views.home,name='home'),
    url(r'^shop/', include('shop.urls')),
    url(r'^push/', include('push.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
   (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
   (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)
