from .models import Shop, Product

from rest_framework import serializers


class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = ('name', 'location', 'introduction', 'products')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'product_type', 'price')