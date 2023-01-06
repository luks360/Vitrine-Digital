from django.urls import path

from .views import HomeView, LoginView

app_name = "main"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login", LoginView.as_view(), name="login"),
]