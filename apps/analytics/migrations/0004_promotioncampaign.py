# Generated by Django 4.1.7 on 2023-08-29 05:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_product_campaign_limit_reached'),
        ('users', '0003_alter_customer_phone_number_and_more'),
        ('analytics', '0003_engagement_customer_ip_engagement_device_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromotionCampaign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('likes', models.PositiveIntegerField(default=0)),
                ('shares', models.PositiveIntegerField(default=0)),
                ('comments', models.PositiveIntegerField(default=0)),
                ('clicks', models.PositiveIntegerField(default=0)),
                ('views', models.PositiveIntegerField(default=0)),
                ('influencer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.influencer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
