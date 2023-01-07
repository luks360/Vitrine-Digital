from django.db import models
from apps.main.models import Clients
from apps.company.models import Products

# Create your models here.
class Requests(models.Model):

    client = models.ForeignKey(Clients, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)