from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.company import serializers
from apps.company.models import Products


# PRODUCTS
@api_view()
def products_api_list(request):
    products = Products.objects.all()
    serializer = serializers.ProductsSerializer(instance=products, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)