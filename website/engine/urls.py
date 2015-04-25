from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from views.auth import do_login, do_logout, do_register, dashboard
from views.edit import ProductCreateView, ProductUpdateView
from views.shop import products, ShopDetailView, ProductDetailView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='engine/index.html'),name="index"),
    url(r'^login/', do_login, name="do_login"),
    url(r'^logout/', do_logout, name="do_logout"),
    url(r'^register/', do_register, name="do_register"),
    url(r'^dashboard/$', dashboard, name="dashboard"),
    url(r'^shops/$', ShopDetailView.as_view(),name='shop_detail'),
    url(r'^shops/products/$', products,name='product_list'),
    url(r'^shops/products/(?P<pk>[\d]+)/$', ProductDetailView.as_view(),name='product_detail'),
    url(r'^shops/products/create/$', ProductCreateView.as_view(),name='product_create'),
    url(r'^shops/products/edit/(?P<pk>[\d]+)/$', ProductUpdateView.as_view(),name='product_update'),
)
