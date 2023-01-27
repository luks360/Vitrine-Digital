
from django.contrib import admin
from django.urls import include, path

from apps.company.api import products_api_list

from .views import DashboardView

app_name = "company"

urlpatterns = [
    path("products/api", products_api_list, name="products_api_list"),
    
    path("dashboard", DashboardView.as_view(), name="dashboard-company"),
]
