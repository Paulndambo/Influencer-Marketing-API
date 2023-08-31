# Generated by Django 4.1.7 on 2023-08-28 12:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Product",
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
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "promotion_budget",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("max_promotion_days", models.FloatField(default=1)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
