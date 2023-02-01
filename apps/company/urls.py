from django.contrib import admin
from django.urls import include, path

from apps.company.api import ProductApiViewSet

from .views import DashboardView, RequestsView

app_name = "company"

urlpatterns = [
    path("products/api", ProductApiViewSet.products_api_list, name="products_api_list"),
    path("dashboard", DashboardView.as_view(), name="dashboard-company"),
    path("requests", RequestsView.as_view(), name="requests-company"),
]
