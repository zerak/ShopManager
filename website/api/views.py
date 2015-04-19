from django.shortcuts import render

from rest_framework import viewsets

from shop.serializers import ShopSerializer, ProductSerializer
from shop.models import Shop, Product

# Create your views here.
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
