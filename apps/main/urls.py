from django.urls import path

from .views import HomeView, LoginView, ShopsView

app_name = "main"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login", LoginView.as_view(), name="login"),
    path("shops", ShopsView.as_view(), name="shops"),   
]
