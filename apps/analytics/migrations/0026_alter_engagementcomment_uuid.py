# Generated by Django 4.2.4 on 2023-09-05 09:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0025_alter_engagementcomment_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagementcomment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('43c9b1a6-0c4c-494e-852a-4d88655a4918')),
        ),
    ]
