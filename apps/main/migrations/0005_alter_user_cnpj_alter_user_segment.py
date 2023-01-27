# Generated by Django 4.1.5 on 2023-01-24 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_user_managers"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="cnpj",
            field=models.CharField(max_length=200, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="user",
            name="segment",
            field=models.CharField(
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
                default=None,
                max_length=200,
            ),
        ),
    ]