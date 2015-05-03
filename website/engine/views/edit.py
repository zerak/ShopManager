from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView, UpdateView

from engine.forms import ShopForm, ProductForm
from engine.models import Shop, Product
from util.mixins import LoginRequiredMixin, ModelActionMixin
from util.custom_view import *

class ProductCreateView(LoginRequiredMixin, ModelActionMixin, CreateView):
    form_class = ProductForm
    template_name = 'shop/product_create.html'

    def get_success_url(self):
        return reverse('product_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        product_form = form
        product_form.shop = get_object_or_404(Shop, pk=self.request.session['shop'])
        return super(ProductCreateView, self).form_valid(form)

class ProductUpdateView(LoginRequiredMixin, ModelActionMixin, UpdateView):
    success_msg = "Product Updated!"
    form_class = ProductForm
    template_name = 'shop/product_edit.html'

    model = Product

    def form_valid(self, form):
        return super(ProductUpdateView, self).form_valid(form)

    def get_success_url(self):
        return reverse('product_list')

class ShopUpdateView(LoginRequiredMixin, ModelActionMixin, UpdateView):
    success_msg = 'Shop Updated!'
    form_class = ShopForm
    template_name = 'shop/shop_edit.html'

    model = Shop

    def get_object(self):
        return get_object_or_404(Shop, pk=self.request.session['shop'])

    def get_success_url(self):
        return reverse('shop_detail')
