# Generated by Django 4.2.5 on 2023-09-08 12:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0039_alter_engagementcomment_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagementcomment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('3f3cc6b5-ca84-49e5-b648-7f7d42bdc280')),
        ),
    ]