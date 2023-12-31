# Generated by Django 4.2.4 on 2023-09-04 10:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0018_promotioncampaign_facebook_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='promotioncampaign',
            name='email_url',
            field=models.URLField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='engagementcomment',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('7c00a3cb-352c-4045-825a-9f8f2b9afbdb')),
        ),
    ]
