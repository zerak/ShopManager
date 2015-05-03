from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView

from engine.models import Shop, New
from engine.forms import NewForm
from util.mixins import LoginRequiredMixin, ModelActionMixin
from util.custom_view import *

class NewCreateView(LoginRequiredMixin, ModelActionMixin, CreateView):
    form_class = NewForm
    template_name = 'shop/new_create.html'

    def get_success_url(self):
        return reverse('new_list')

    def form_valid(self, form):
        new_form = form
        new_form.shop = get_object_or_404(Shop, pk=self.request.session['shop'])
        return super(NewCreateView, self).form_valid(form)

class NewListView(LoginRequiredMixin, ListSearchView):
    model = New
    template_name ='shop/new_list.html'

    def get_object(self, *args, **kw):
        return get_object_or_404(New, shop_id=self.request.session['shop'])