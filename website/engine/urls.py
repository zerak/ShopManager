from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from views.auth import do_login, do_logout, do_register, dashboard
from views.shop import ShopListView, ProductListView, ShopDetailView, ProductDetailView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='engine/index.html'),name="index"),
    url(r'^login/', do_login, name="do_login"),
    url(r'^logout/', do_logout, name="do_logout"),
    url(r'^register/', do_register, name="do_register"),
    url(r'^dashboard/$', dashboard, name="dashboard"),
    url(r'^shops/$', ShopListView.as_view(), name="shop_list"),
    url(r'^shops/(?P<pk>[0-9]+)/$', ShopDetailView.as_view(),name='shop_detail'),
    url(r'^products/$', ProductListView.as_view(),name='product_list'),
    url(r'^products/(?P<pk>[0-9]+)/$', ProductDetailView.as_view(),name='product_detail'),
)
