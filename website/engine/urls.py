from django.conf.urls import patterns,include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic import TemplateView

from . import views

urlpatterns = patterns('',
    # Examples:
    url(r'^$', TemplateView.as_view(template_name='engine/index.html'),name="index"),
    url(r'^login/', views.do_login, name="do_login"),
    url(r'^logout/', views.do_logout, name="do_logout"),
    url(r'^register/', views.do_register, name="do_register"),
    url(r'^dashboard/', views.dashboard, name="dashboard"),
)
