from django.db import models

from apps.main.models import User


class Products(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    image = models.ImageField()
    store = models.ForeignKey(User, on_delete=models.CASCADE)