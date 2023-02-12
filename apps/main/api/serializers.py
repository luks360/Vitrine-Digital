from rest_framework import serializers

from apps.main import models


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Stores
        fields = ["id", "cnpj", "corporate_name", "email", "contact", "segment", "logo"]


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Clients
        fields = ["id", "name", "last_name", "email", "password", "birth_date", "icon"]
