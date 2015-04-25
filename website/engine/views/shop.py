from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from engine.models import Shop, Product
from util.mixins import LoginRequiredMixin
from util.custom_view import *

# Create your views here.

@login_required
def products(request):
    if request.method == 'GET':
        shop = request.user.own_shop
        if shop:
            products = shop.product_set.all()
            q = request.GET.get('q')
            if q:
                products = products.filter(name__icontains=q)
            return render(request,
                                    'shop/product_list.html',
                                    dict(product_list=products)
                        )
        return HttpResponse('You are not the store')
    return HttpResponse('')

class ShopDetailView(LoginRequiredMixin, CustomDetailView):

    def get(self, *args, **kw):
        shop = self.request.user.own_shop
        return render(self.request,
                                'shop/shop_detail.html',
                                dict(shop=shop)
                    )


class ProductDetailView(LoginRequiredMixin, CustomDetailView):
    model = Product
    template_name = 'shop/product_detail.html'

