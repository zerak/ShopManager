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
