# Generated by Django 4.2.5 on 2023-09-08 12:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0038_alter_engagementcomment_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagementcomment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('0fe1d06d-1dd9-44a1-8b26-511c7818a804')),
        ),
    ]