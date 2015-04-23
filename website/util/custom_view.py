#-*- coding:utf-8 -*-
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView

class ListFilterView(ListView):
    list_model = None

    def get_queryset(self):
        if self.list_model is not None:
            return self.list_model.objects.filter()
        return []

class CustomDetailView(DetailView):
    model = None

    def get_context_data(self, **kwargs):
        context = super(ShopDetailView, self).get_context_data(**kwargs)
        return context

class ListRelated(DetailView, ListView):
    related_name = None

    def get_list_queryset(self):
        obj = self.get_detail_object()
        return getattr(obj, self.related_name).all()