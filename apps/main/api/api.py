from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.company.models import Products
from apps.main.api import serializers
from apps.main.models import Clients, Stores


# STORES
@api_view()
def store_api_list(request):
    stores = Stores.objects.all()
    serializer = serializers.StoreSerializer(instance=stores, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def store_api_unique(request, id):
    stores = Stores.objects.get(id=id)
    serializer = serializers.StoreSerializer(instance=stores, many=False)    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=['POST'])
def store_api_create(request):
    
    serializer = serializers.StoreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    


# CLIENTS
@api_view(http_method_names=['POST'])
def clients_api_create(request):
    print(request.data)
    serializer = serializers.ClientsSerializer(data=request.data) 
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view()
def clients_api_list(request):
    clients = Clients.objects.all()
    serializer = serializers.ClientsSerializer(instance=clients, many=True) 
    
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view()
def clients_api_unique(request, id):
    clients = Clients.objects.get(id=id)
    serializer = serializers.ClientsSerializer(instance=clients, many=False)
    
    return Response(serializer.data, status=status.HTTP_200_OK)


# PRODUCTS
@api_view()
def products_api_list(request):
    products = Products.objects.all()
    serializer = serializers.ProductSerializer(instance=products, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)