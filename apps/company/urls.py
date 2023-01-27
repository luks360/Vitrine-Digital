
from django.contrib import admin
from django.urls import include, path

from apps.company.api import products_api_list

app_name = "company"

urlpatterns = [
    path("products/api", products_api_list, name="products_api_list"),
    
]
