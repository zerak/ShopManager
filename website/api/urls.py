from django.conf.urls import patterns,include, url

from rest_framework import routers

from api.views import ShopViewSet, ProductViewSet
from . import views

router = routers.DefaultRouter()
router.register(r'shops', ShopViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
)
