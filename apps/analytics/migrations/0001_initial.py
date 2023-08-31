# Generated by Django 4.1.7 on 2023-08-28 12:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("products", "0001_initial"),
        ("users", "0002_influencer_customer"),
    ]

    operations = [
        migrations.CreateModel(
            name="Engagement",
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
                ("likes", models.PositiveIntegerField(default=0)),
                ("shares", models.PositiveIntegerField(default=0)),
                ("comments", models.PositiveIntegerField(default=0)),
                ("clicks", models.PositiveIntegerField(default=0)),
                ("views", models.PositiveIntegerField(default=0)),
                (
                    "influencer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="users.influencer",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="products.product",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
