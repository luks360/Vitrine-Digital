from django.urls import path

from .views import (AboutView, ContactView, HomeView, LoginView, RegisterView,
                    ShopsView, StoreView)

app_name = "main"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login", LoginView.as_view(), name="login"),
    path("shops", ShopsView.as_view(), name="shops"),   
    path("about", AboutView.as_view(), name="about"),
    path("contact", ContactView.as_view(), name="contact"),
    path("register", RegisterView.as_view(), name="register"),
    path("store", StoreView.as_view(), name="store"),
    
]
