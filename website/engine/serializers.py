from .models import Shop, Product, New

from rest_framework import serializers

class NewSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = New
        fields = ('title', 'body', 'add_date')

class ShopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Shop
        fields = ('name', 'location', 'introduction')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'product_type', 'price', 'shop')