import os
import random
import uuid

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import redirect, render
from django.views import View

from apps.company.models import Products
from apps.main.forms import (
    LoginClientForm,
    LoginStoreForm,
    RegisterClientForm,
    RegisterStoreForm,
)
from apps.main.models import Clients, Stores

PER_PAGE = os.environ.get("PER_PAGE", 12)
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

        products = Products.objects.all()
        productsV = []
        if products is not None:  # pragma: no cover
            if len(products) >= 3:
                productsV = random.sample(list(products), 3)
            elif len(products) == 2:
                productsV = random.sample(list(products), 2)
            elif len(products) == 1:
                productsV = random.sample(list(products), 1)

        items = {"categories": categories, "products": productsV}

        return render(request, "index.html", items)


class LoginView(LoginView):

    forms = {
        "form_client": LoginClientForm(),
        "form_store": LoginStoreForm(),
    }

    def post(self, request):
        name = request.POST.get("name", False)
        if name != False:
            name = request.POST["name"]
            password = request.POST["password"]
            user_client = authenticate(request, username=name, password=password)
            if user_client is not None:  # pragma: no cover
                login(request, user_client)
                return redirect("/")
        else:
            name = request.POST["corporate_name"]
            password = request.POST["password"]
            user_loja = authenticate(request, username=name, password=password)
            if user_loja is not None:  # pragma: no cover
                login(request, user_loja)
                return redirect("/dashboard")

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
                client_form.save()
                messages.success(request, "Cadastrado com sucesso!")

        if store_form:  # pragma: no cover
            if store_form.is_valid():
                store_form.save()
                messages.success(request, "Cadastrado com sucesso!")

        return render(request, "sign-up.html", self.forms)

    def get(self, request):

        return render(request, "sign-up.html", self.forms)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("/login")


class ShopsView(View):
    def get(self, request, segment):

        stores = Stores.objects.filter(segment=segment)
        paginator = Paginator(stores, PER_PAGE)
        page = request.GET.get("page")
        storesP = paginator.get_page(page)

        items = {"stores": storesP}

        return render(request, "shops.html", items)


class StoreView(View):
    def get(self, request, id):

        store = Stores.objects.get(id=id)
        products = Products.objects.filter(store__id=id)

        item = {
            "store": store,
            "products": products,
        }
        return render(request, "store.html", item)


class AboutView(View):
    def get(self, request):

        return render(request, "about.html")


class ContactView(View):
    def get(self, request):

        return render(request, "contact.html")
