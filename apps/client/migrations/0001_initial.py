# Generated by Django 4.1.5 on 2023-01-18 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("main", "0001_initial"),
        ("company", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Requests",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "client",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.clients"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="company.products",
                    ),
                ),
            ],
        ),
    ]
