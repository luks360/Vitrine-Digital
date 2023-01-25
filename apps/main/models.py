import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin

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

class User(AbstractBaseUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cnpj = models.CharField(max_length=200, unique=True, null=True)
    name = models.CharField(max_length=200)
    birth_date = models.DateField(null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    contact = models.CharField(max_length=200, null=True)
    segment = models.CharField(
        max_length = 200,
        choices = SEGMENT_CHOICES,
        default = '-------------',
        null=True
    )
    icon = models.ImageField(upload_to = "icons/")
    is_client = models.BooleanField(default=False)
    is_store = models.BooleanField(default=False)
    objects = UserManager()

    USERNAME_FIELD = "email"