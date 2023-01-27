from django.contrib import admin

from apps.main.models import Clients, Stores

# Register your models here.

admin.site.register(Clients)
admin.site.register(Stores)