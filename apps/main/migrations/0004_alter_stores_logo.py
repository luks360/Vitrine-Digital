# Generated by Django 4.1.4 on 2023-01-11 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0003_alter_stores_logo"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stores",
            name="logo",
            field=models.ImageField(upload_to="logos/"),
        ),
    ]
