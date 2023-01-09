from django.urls import path

from .views import HomeView, LoginView, AboutView, ContactView, RegisterView

app_name = "main"
urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("login", LoginView.as_view(), name="login"),
    path("about", AboutView.as_view(), name="about"),
    path("contact", ContactView.as_view(), name="contact"),
    path("register", RegisterView.as_view(), name="register"),
]
