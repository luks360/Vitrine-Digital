from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

from .api.api import (clients_api_create, clients_api_list, clients_api_unique,
                      products_api_list, store_api_create, store_api_list,
                      store_api_unique)
from .views import (AboutView, ContactView, HomeView, LoginView, LogoutView,
                    RegisterView, ShopsView, StoreView)

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
    path("stores/api/create", store_api_create, name="stores_api_create"),
    path("stores/api", store_api_list, name="stores_api"),
    path("stores/api/<str:id>", store_api_unique, name="stores_api_unique"),
    path("clients/api/create", clients_api_create, name="clients_api_create"),
    path("clients/api", clients_api_list, name="clients_api"),
    path("clients/api/<str:id>", clients_api_unique, name="clients_api_unique"),
    
    
]

if settings.DEBUG: # pragma: no cover
        urlpatterns += static (settings.MEDIA_URL,
                              document_root = settings.MEDIA_ROOT)
