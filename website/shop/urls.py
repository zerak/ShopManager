from django.conf.urls import patterns,include, url
from views import *

urlpatterns = patterns('',
    url(r'^$', home, name='home_page'),
    url(r'^shop_list$', ShopListView.as_view(),name='shop_list_page'),
    url(r'^product_list$', ProductListView.as_view(),name='product_list_page'),
)
