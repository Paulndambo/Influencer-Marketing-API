# Generated by Django 4.2.4 on 2023-09-05 07:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0023_alter_engagementcomment_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagementcomment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('cb7ab1f5-17f3-463e-baab-42b08837276c')),
        ),
    ]
