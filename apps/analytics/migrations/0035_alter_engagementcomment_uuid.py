# Generated by Django 4.2.5 on 2023-09-08 08:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0034_alter_engagementcomment_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagementcomment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('ad0f35c9-4919-480f-ba29-7881f5805686')),
        ),
    ]
