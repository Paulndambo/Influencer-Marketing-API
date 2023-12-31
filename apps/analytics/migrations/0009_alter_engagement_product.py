# Generated by Django 4.2.4 on 2023-09-01 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_alter_product_promotion_ends_on'),
        ('analytics', '0008_promotioncampaign_influencer_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagement',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productengagements', to='products.product'),
        ),
    ]
