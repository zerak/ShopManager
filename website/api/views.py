from django.shortcuts import render

from rest_framework import viewsets

from engine.serializers import ShopSerializer, ProductSerializer
from engine.models import Shop, Product

# Create your views here.
class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
