# Generated by Django 4.1.7 on 2023-08-31 11:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0005_product_promotion_ends_on"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="promotion_ends_on",
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]