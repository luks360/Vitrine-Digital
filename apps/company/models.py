from django.db import models

from apps.main.models import Stores


class Products(models.Model):

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2,max_digits=10)
    image = models.ImageField(upload_to = "image-products/")
    store = models.ForeignKey(Stores, on_delete=models.CASCADE)