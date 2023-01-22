# Generated by Django 4.1.5 on 2023-01-18 19:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Clients",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("last_name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=200)),
                ("birth_date", models.DateField()),
                ("icon", models.ImageField(upload_to="")),
            ],
        ),
        migrations.CreateModel(
            name="Stores",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("cnpj", models.CharField(max_length=200)),
                ("corporate_name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(max_length=200)),
                ("contact", models.CharField(max_length=200)),
                (
                    "segment",
                    models.CharField(
                        choices=[
                            ("Cosméticos", "Cosméticos"),
                            ("Confecções", "Confecções"),
                            ("Bijuterias", "Bijuterias"),
                            ("Construção e ferramentas", "Construção e ferramentas"),
                            ("Alimentação", "Alimentação"),
                            ("Variedades", "Variedades"),
                            ("Calçados", "Calçados"),
                            ("Decoração", "Decoração"),
                            ("Eletrônicos", "Eletrônicos"),
                        ],
                        default="-------------",
                        max_length=200,
                    ),
                ),
                ("logo", models.ImageField(upload_to="logos/")),
            ],
        ),
    ]
