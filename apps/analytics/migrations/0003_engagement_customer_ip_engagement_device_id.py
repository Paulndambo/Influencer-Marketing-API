# Generated by Django 4.1.7 on 2023-08-28 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_engagement_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='engagement',
            name='customer_ip',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='engagement',
            name='device_id',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
