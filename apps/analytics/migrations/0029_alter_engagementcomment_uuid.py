# Generated by Django 4.2.5 on 2023-09-06 09:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0028_alter_engagementcomment_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagementcomment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('c9d8bfe1-2b04-449b-86af-6c6c8b1f63d3')),
        ),
    ]
