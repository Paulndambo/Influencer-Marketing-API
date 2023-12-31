# Generated by Django 4.1.7 on 2023-08-31 07:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("products", "0003_product_campaign_limit_reached"),
        ("analytics", "0006_alter_promotioncampaign_influencer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="promotioncampaign",
            name="product",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="productcampaigns",
                to="products.product",
            ),
        ),
    ]
