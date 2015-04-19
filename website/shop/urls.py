from django.conf.urls import patterns,include, url
from views import *

urlpatterns = patterns('',
    url(r'^$', home, name='home_page'),
    url(r'^shops$', ShopListView.as_view(),name='shop_list_page'),
    url(r'^shops/(?P<pk>[0-9]+)/$', ShopDetailView.as_view(),name='shop_detail'),
    url(r'^products$', ProductListView.as_view(),name='product_list_page'),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetailView.as_view(),name='product_detail'),
)
