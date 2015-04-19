from django.shortcuts import render
from util.custom_view import *

from .models import Shop, Product

def home(request):
    return render(request, 'shop/index.html')

# Create your views here.
class ShopListView(ListFilterView):
    list_model = Shop
    template = 'shop/shop_list.html'
    context_object_name = 'shop_list'

class ProductListView(ListFilterView):
    list_model = Product
    template_name = 'shop/product_list.html'
    context_object_name = 'product_list'

class ShopDetailView(CustomDetailView):
    model = Shop
    template_name = 'shop/shop_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ShopDetailView, self).get_context_data(**kwargs)
        return context

class ProductDetailView(CustomDetailView):
    model = Product
    template = 'shop/product_detail.html'

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        return context