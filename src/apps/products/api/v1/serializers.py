from rest_framework import serializers
from apps.products.models import Product


class ProductSerializer(serializers.ModelSerializer):
    brand_name = serializers.CharField(read_only=True)

    class Meta:
        model = Product
        fields = ('id', 'sku', 'name', 'price', 'brand_name')
