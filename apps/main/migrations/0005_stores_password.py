# Generated by Django 4.1.4 on 2023-01-11 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0004_alter_stores_logo"),
    ]

    operations = [
        migrations.AddField(
            model_name="stores",
            name="password",
            field=models.CharField(default=123, max_length=200),
            preserve_default=False,
        ),
    ]