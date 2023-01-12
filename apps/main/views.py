from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View

from apps.main.forms import RegisterClientForm, RegisterStoreForm

categories = [
    "Cosméticos",
    "Confecções",
    "Bijuterias",
    "Construção e ferramentas",
    "Alimentação",
    "Variedades",
    "Calçados",
    "Decoração",
    "Eletrônicos",
]


class HomeView(View):
    def get(self, request):

        return render(request, "index.html", {"categories": categories})


class LoginView(LoginView):
    redirect_authenticated_user = True
    template_name = "login.html"


    def get_success_url(self):
        return reverse_lazy("index")

    def form_invalid(self, form):
        messages.error(self.request, "Inválido Login e Senha.")
        return self.render_to_response(self.get_context_data(form=form))

class RegisterView(View):

    forms = {
        "form_client": RegisterClientForm(),
        "form_store": RegisterStoreForm(),
    }

    def get(self, request):

        return render(request, "sign-up.html", self.forms)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return reverse("login")

class ShopsView(View):
    def get(self, request):
        return render(request, "shops.html", context={
            'segment': 'Alimentação',
        })
    
class StoreView(View):
    def get(self, request):
        return render(request, "store.html", context={
            'segment': 'Alimentação',
        })
class AboutView(View):

    def get(self, request):

        return render(request, "about.html")

class ContactView(View):

    def get(self, request):

        return render(request, "contact.html")
