
from rest_framework import serializers

from apps.company import models


class ProductsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Products
        fields = ['name', 'description', 'price', 'image', 'store']

        