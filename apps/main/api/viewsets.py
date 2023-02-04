from django.db import connection
from drf_yasg.utils import swagger_auto_schema
from iteration_utilities import duplicates
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

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


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_store_api(request, id):
    stores = models.Stores.objects.get(id=id)
    stores.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


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


@swagger_auto_schema(
    method="POST",
    request_body=serializers.StoreSerializer,
)
@api_view(http_method_names=["POST"])
@permission_classes([IsAuthenticated])
def update_store_api(request, id):

    stores = models.Stores.objects.get(id=id)
    serializer = serializers.StoreSerializer(instance=stores, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def store_report(request):
    with connection.cursor() as cursor:
        query_list_stores = "SELECT main_stores.id, main_stores.corporate_name, count(company_products.id) as quantity, company_products.name as product_name FROM main_stores JOIN company_products ON main_stores.id = company_products.store_id GROUP BY main_stores.id, main_stores.corporate_name, company_products.name"
        cursor.execute(query_list_stores)
        rows_stores = cursor.fetchall()
        query_produtos = "SELECT company_products.id,main_stores.id,company_products.name FROM main_stores INNER JOIN company_products ON main_stores.id = company_products.store_id"
        cursor.execute(query_produtos)
        rows_products = cursor.fetchall()
        chave_stores = ("Id", "Empresa", "Quantidade", "Produto")
        chave_products = ("Id do produto", "Id da loja", "produto")

        list_stores = []
        list_products = []
        for row in rows_stores:
            list_stores.append(dict(zip(chave_stores, row)))

        for row in rows_products:
            list_products.append(dict(zip(chave_products, row)))
        for product in list_stores:
            product["Produto"] = []

        for row in list_stores:
            for i in list_products:
                if row["Id"] == i["Id da loja"]:
                    row["Produto"].append(i["produto"])

        for i in list_stores:
            i["Quantidade"] = len(i["Produto"])

        dup = list(duplicates(list_stores))
        for i in range(len(dup)):
            list_stores.remove(dup[i])
    return Response(list_stores, status.HTTP_200_OK)


# CLIENTS
@swagger_auto_schema(
    method="POST",
    request_body=serializers.ClientsSerializer,
)
@api_view(http_method_names=["POST"])
@permission_classes([IsAuthenticated])
def clients_api_create(request):
    serializer = serializers.ClientsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(
    method="POST",
    request_body=serializers.ClientsSerializer,
)
@api_view(http_method_names=["POST"])
@permission_classes([IsAuthenticated])
def update_client_api(request, id):
    client = models.Clients.objects.get(id=id)
    serializer = serializers.ClientsSerializer(instance=client, data=request.data)
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


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_client_api(request, id):
    client = models.Clients.objects.get(id=id)
    client.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
