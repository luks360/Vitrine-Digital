from django.contrib import admin
from django.urls import include, path

from apps.company.api import ProductApiViewSet

from .views import DashboardView, RequestsView

app_name = "company"

urlpatterns = [
    path("products/api", ProductApiViewSet.products_api_list, name="products_api_list"),
    path(
        "products/api/<int:id>",
        ProductApiViewSet.product_api_unique,
        name="products_api_list",
    ),
    path(
        "products/api/create",
        ProductApiViewSet.product_api_create,
        name="products_api_list",
    ),
    path(
        "products/api/delete/<int:id>",
        ProductApiViewSet.delete_product_api,
        name="products_api_list",
    ),
    path(
        "products/api/update/<int:id>",
        ProductApiViewSet.update_product_api,
        name="products_api_list",
    ),
    path("dashboard", DashboardView.as_view(), name="dashboard-company"),
    path("requests", RequestsView.as_view(), name="requests-company"),
]
