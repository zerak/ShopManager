from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from rest_framework import routers

from api.views import ShopViewSet, ProductViewSet, NewViewSet

router = routers.DefaultRouter()
router.register(r'shops', ShopViewSet)
router.register(r'products', ProductViewSet)
router.register(r'news', NewViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^engine/', include('engine.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
   (r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
   (r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)
