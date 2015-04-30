from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from engine.models import Shop, Product
from util.mixins import LoginRequiredMixin
from util.custom_view import *

# Create your views here.
class ProductListView(LoginRequiredMixin, ListSearchView):
    model = Product
    template_name ='shop/product_list.html'

    def get_object(self, *args, **kw):
        return get_object_or_404(Product, shop_id=self.request.session['shop'])

class ProductDetailView(LoginRequiredMixin, CustomDetailView):
    model = Product
    template_name = 'shop/product_detail.html'

class ShopDetailView(LoginRequiredMixin, CustomDetailView):

    def get(self, *args, **kw):
        shop = get_object_or_404(Shop, pk=self.request.session['shop'])
        return render(self.request,
                                'shop/shop_detail.html',
                                dict(shop=shop)
                    )