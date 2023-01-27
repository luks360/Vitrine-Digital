from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views import View
from apps.main.forms import RegisterClientForm, RegisterStoreForm, LoginClientForm, LoginStoreForm
from apps.main.models import User
from apps.company.models import Products

# Create your views here.

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

    forms = {
        "form_client": LoginClientForm(),
        "form_store": LoginStoreForm(),
    }

    def post(self, request):
        user_aux = User.objects.get(email=request.POST["email"])
        password = request.POST["password"]
        user = authenticate(request, email=user_aux.email, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")

        return render(request, "login.html", self.forms)

    def get(self, request):

        return render(request, "login.html", self.forms)

class RegisterView(View):

    forms = {
        "form_client": RegisterClientForm(),
        "form_store": RegisterStoreForm(),
    }

    def post(self, request):
        
        client_form = RegisterClientForm(request.POST, request.FILES)
        store_form = RegisterStoreForm(request.POST, request.FILES)

        if client_form:  # pragma: no cover
            if client_form.is_valid():
                client = client_form.save(commit=False)
                client.is_client = True
                client.save()
                return redirect("/login")

        if store_form:
            if store_form.is_valid():
                store = store_form.save(commit=False)
                store.is_store = True
                store.save()
                return redirect("/login")

        return render(request, "sign-up.html", self.forms)

    def get(self, request):

        return render(request, "sign-up.html", self.forms)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/login")

class ShopsView(View):
    def get(self, request, segment):

        stores = User.objects.filter(segment=segment)

        items = {
            "stores": stores
        }

        return render(request, "shops.html", items)
    
class StoreView(View):

    def get(self, request, id):

        store = User.objects.get(id=id)
        products = Products.objects.filter(store__id=id)
        print(store)
        item = {
            'store': store,
            'products': products,
        }

        return render(request, "store.html", item)
    
class AboutView(View):

    def get(self, request):

        return render(request, "about.html")

class ContactView(View):

    def get(self, request):

        return render(request, "contact.html")