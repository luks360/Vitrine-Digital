import uuid
from django.db import models

# Create your models here.

SEGMENT_CHOICES = (
    ("Cosméticos", "Cosméticos"),
    ("Confecções", "Confecções"),
    ("Bijuterias", "Bijuterias"),
    ("Construção e ferramentas", "Construção e ferramentas"),
    ("Alimentação", "Alimentação"),
    ("Variedades", "Variedades"),
    ("Calçados", "Calçados"),
    ("Decoração", "Decoração"),
    ("Eletrônicos", "Eletrônicos"),
)

class Stores(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cnpj = models.CharField(max_length=200)
    corporate_name = models.CharField(max_length=200)
    email = models.EmailField()
    contact = models.CharField(max_length=200)
    segment = models.CharField(
        max_length = 200,
        choices = SEGMENT_CHOICES,
        default = '-------------'
    )

class Clients(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    birth_date = models.DateField()