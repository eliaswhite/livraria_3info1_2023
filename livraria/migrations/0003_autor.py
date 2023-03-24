# Generated by Django 4.1.7 on 2023-03-24 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("livraria", "0002_editora"),
    ]

    operations = [
        migrations.CreateModel(
            name="Autor",
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
                ("nome", models.CharField(max_length=255)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
            ],
        ),
    ]
