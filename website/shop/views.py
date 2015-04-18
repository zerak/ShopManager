from django.shortcuts import render
from util.custom_view import *

from .models import Shop, Product

def home(request):
    return render(request, 'shop/index.html')

# Create your views here.
class ShopListView(ListFilterView):
    template = 'shop/shop_list.html'
    list_model = Shop

    def get_context_data(self, **kwargs):
        context = super(ShopListView, self).get_context_data(**kwargs)
        return context

class ProductListView(ListFilterView):
    template = 'shop/product_list.html'
    list_model = Product

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        return context