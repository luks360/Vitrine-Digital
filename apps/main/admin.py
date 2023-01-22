from django.contrib import admin

from apps.main.models import Clients, Stores

# Register your models here.

admin.site.register(Stores)
admin.site.register(Clients)
