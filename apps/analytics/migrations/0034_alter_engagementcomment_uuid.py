# Generated by Django 4.2.5 on 2023-09-08 08:31

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0033_alter_engagementcomment_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagementcomment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('4fee5372-47f6-4932-bc75-e66e1856d817')),
        ),
    ]
