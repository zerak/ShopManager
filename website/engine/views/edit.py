from django.shortcuts import render
from django.views.generic import CreateView, UpdateView

from engine.forms import ProductForm
from engine.models import Shop, Product
from util.mixins import LoginRequiredMixin, ModelActionMixin

class ProductCreateView(LoginRequiredMixin, ModelActionMixin, CreateView):
    success_url = '/engine/shops/products'

    form_class = ProductForm
    template_name = 'shop/product_create.html'

    def form_valid(self, form):
        product_form = form
        product_form.shop = self.request.user.own_shop
        return super(ProductCreateView, self).form_valid(form)

class ProductUpdateView(LoginRequiredMixin, ModelActionMixin, UpdateView):
    success_msg = "Product Updated!"

    form_class = ProductForm
    template_name = 'shop/product_edit.html'
