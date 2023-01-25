from django.db import models

from apps.company.models import Products
from apps.main.models import User


class Requests(models.Model):

    client = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)