from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

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
    
    
]

if settings.DEBUG: # pragma: no cover
        urlpatterns += static (settings.MEDIA_URL,
                              document_root = settings.MEDIA_ROOT)
