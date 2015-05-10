from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from views.auth import do_login, do_logout, do_register, reset_passwd, dashboard
from views.edit import ShopUpdateView, ProductCreateView, ProductUpdateView
from views.ads import index, AdsView
from views.geo import geo
from views.stat import stat, data
from views.shop import ProductListView, ShopDetailView, ProductDetailView
from views.new import NewCreateView, NewListView, NewUpdateView, NewDeleteView
from views.calendar import  EventsView, all_events

urlpatterns = patterns('',
    # auth:
    url(r'^$', TemplateView.as_view(template_name='engine/index.html'),name="index"),
    url(r'^login/', do_login, name="do_login"),
    url(r'^logout/', do_logout, name="do_logout"),
    url(r'^register/', do_register, name="do_register"),
    url(r'^reset/$', reset_passwd, name="do_reset"),
    url(r'^dashboard/$', dashboard, name="dashboard"),

    # shop:
    url(r'^shops/$', ShopDetailView.as_view(), name='shop_detail'),
    url(r'^shops/edit/$', ShopUpdateView.as_view(), name='shop_update'),
    url(r'^shops/ads/$', index, name='ads'),
    url(r'^shops/geo/$', geo, name='geo'),
    url(r'^shops/data/$', data, name='shop_data'),
    url(r'^shops/stat/$', stat, name='stat'),
    url(r'^shops/news/$', NewListView.as_view(),name='new_list'),
    url(r'^shops/news/create/$', NewCreateView.as_view(),name='new_create'),
    url(r'^shops/news/edit/(?P<pk>[\d]+)/$', NewUpdateView.as_view(),name='new_update'),
    url(r'^shops/news/delete/(?P<pk>[\d]+)/$', NewDeleteView.as_view(),name='new_delete'),
    url(r'^shops/products/$', ProductListView.as_view(),name='product_list'),
    url(r'^shops/products/(?P<pk>[\d]+)/$', ProductDetailView.as_view(),name='product_detail'),
    url(r'^shops/products/create/$', ProductCreateView.as_view(),name='product_create'),
    url(r'^shops/products/edit/(?P<pk>[\d]+)/$', ProductUpdateView.as_view(),name='product_update'),

    url(r'^shops/calendar$', EventsView.as_view(), name='calendar'),
    url(r'^shops/all_events/', all_events, name='all_events'),
)
