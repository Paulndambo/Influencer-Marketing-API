# Generated by Django 4.2.4 on 2023-09-04 06:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0012_alter_engagement_influencer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='engagementcomment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('2b685301-3831-4461-a43d-eca765c9af63')),
        ),
    ]
