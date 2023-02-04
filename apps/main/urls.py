from django.conf import settings
from django.conf.urls.static import static
from django.db import router
from django.urls import include, path
from rest_framework import permissions, routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.main.api import viewsets

from .views import (
    AboutView,
    ContactView,
    HomeView,
    LoginView,
    LogoutView,
    RegisterView,
    ShopsView,
    StoreView,
)

route = routers.DefaultRouter()

route.register(r"autentication", viewsets.MainApiViewSet, basename="autentication")

app_name = "main"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login", LoginView.as_view(), name="login"),
    path("shops/<str:segment>", ShopsView.as_view(), name="shops"),
    path("about", AboutView.as_view(), name="about"),
    path("contact", ContactView.as_view(), name="contact"),
    path("register", RegisterView.as_view(), name="register"),
    path("store/<str:id>", StoreView.as_view(), name="store"),
    path("logout", LogoutView.as_view(), name="logout"),
    # Api
    path("stores/api/create", viewsets.store_api_create, name="stores_api_create"),
    path("stores/api", viewsets.store_api_list, name="stores_api"),
    path("stores/api/<str:id>", viewsets.store_api_unique, name="stores_api_unique"),
    path(
        "clients/api/create",
        viewsets.clients_api_create,
        name="clients_api_create",
    ),
    path("clients/api", viewsets.clients_api_list, name="clients_api"),
    path(
        "clients/api/<str:id>",
        viewsets.clients_api_unique,
        name="clients_api_unique",
    ),
    path(
        "stores/report/api",
        viewsets.store_report,
        name="store_report",
    ),
    path(
        "stores/update/api/<str:id>",
        viewsets.update_store_api,
        name="store_report",
    ),
    path(
        "stores/delete/api/<str:id>",
        viewsets.delete_store_api,
        name="store_report",
    ),
    path(
        "clients/update/api/<str:id>",
        viewsets.update_client_api,
        name="store_report",
    ),
    path(
        "clients/delete/api/<str:id>",
        viewsets.delete_client_api,
        name="store_report",
    ),
]

if settings.DEBUG:  # pragma: no cover
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
