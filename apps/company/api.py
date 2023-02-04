from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.company import serializers
from apps.company.models import Products


class ProductApiViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProductsSerializer
    queryset = Products.objects.all()
    permission_classes = [
        IsAuthenticated,
    ]

    # PRODUCTS
    @api_view()
    def products_api_list(request):
        products = Products.objects.all()
        serializer = serializers.ProductsSerializer(instance=products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @api_view(["GET"])
    def product_api_unique(request, id):
        product = Products.objects.get(id=id)
        serializer = serializers.ProductsSerializer(instance=product, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        method="POST",
        request_body=serializers.ProductsSerializer,
    )
    @api_view(http_method_names=["POST"])
    def product_api_create(request):
        serializer = serializers.ProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @api_view(["DELETE"])
    def delete_product_api(request, id):
        product = Products.objects.get(id=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    @api_view(http_method_names=["POST"])
    def update_product_api(request, id):
        products = Products.objects.get(id=id)
        serializer = serializers.ProductsSerializer(
            instance=products, data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
