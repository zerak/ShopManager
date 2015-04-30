#-*- coding:utf-8 -*-
from django.views.generic import ListView
from django.views.generic.base import RedirectView
from django.views.generic.detail import DetailView

class ListSearchView(ListView):

    def get_queryset(self):
        queryset = super(ListSearchView, self).get_queryset()
        q = self.request.GET.get('q')
        if q:
            return queryset.filter(name__icontains=q)
        return queryset

class CustomDetailView(DetailView):
    model = None

    def get_context_data(self, **kwargs):
        context = super(CustomDetailView, self).get_context_data(**kwargs)
        return context

class ListRelated(DetailView, ListView):
    related_name = None

    def get_list_queryset(self):
        obj = self.get_detail_object()
        return getattr(obj, self.related_name).all()

