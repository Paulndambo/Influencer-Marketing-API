# Generated by Django 4.2.5 on 2023-09-09 07:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0040_alter_engagementcomment_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagementcomment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('7822c34d-c1c5-431d-a3dc-74a6659fd3ec')),
        ),
    ]
