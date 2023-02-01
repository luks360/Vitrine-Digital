from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.company.models import Products
from apps.main import models
from apps.main.api import serializers


class MainApiViewSet(viewsets.ModelViewSet):
    permission_classes = [
        IsAuthenticated,
    ]
    serializer_class = serializers.StoreSerializer
    queryset = models.Stores.objects.all()

    # STORES


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def store_api_list(request):
    stores = models.Stores.objects.all()
    serializer = serializers.StoreSerializer(instance=stores, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def store_api_unique(request, id):
    stores = models.Stores.objects.get(id=id)
    serializer = serializers.StoreSerializer(instance=stores, many=False)
    return Response(serializer.data, status=status.HTTP_200_OK)


@swagger_auto_schema(
    method="POST",
    request_body=serializers.StoreSerializer,
)
@api_view(http_method_names=["POST"])
@permission_classes([IsAuthenticated])
def store_api_create(request):

    serializer = serializers.StoreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


# CLIENTS
@swagger_auto_schema(
    method="POST",
    request_body=serializers.ClientsSerializer,
)
@api_view(http_method_names=["POST"])
@permission_classes([IsAuthenticated])
def clients_api_create(request):
    print(request.data)
    serializer = serializers.ClientsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def clients_api_list(request):
    clients = models.Clients.objects.all()
    serializer = serializers.ClientsSerializer(instance=clients, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def clients_api_unique(request, id):
    clients = models.Clients.objects.get(id=id)
    serializer = serializers.ClientsSerializer(instance=clients, many=False)

    return Response(serializer.data, status=status.HTTP_200_OK)


# PRODUCTS
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def products_api_list(request):
    products = Products.objects.all()
    serializer = serializers.ProductSerializer(instance=products, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
