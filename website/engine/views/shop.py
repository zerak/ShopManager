from django.shortcuts import render

from engine.models import Shop, Product
from util.mixins import LoginRequiredMixin
from util.custom_view import *

# Create your views here.
class ShopListView(LoginRequiredMixin, ListFilterView):
    list_model = Shop
    template_name = 'shop/shop_list.html'
    context_object_name = 'shop_list'


class ProductListView(LoginRequiredMixin, ListFilterView):
    list_model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'product_list'


class ShopDetailView(LoginRequiredMixin, CustomDetailView):
    model = Shop
    template_name = 'shop/shop_detail.html'


class ProductDetailView(LoginRequiredMixin, CustomDetailView):
    model = Product
    template_name = 'shop/product_detail.html'

