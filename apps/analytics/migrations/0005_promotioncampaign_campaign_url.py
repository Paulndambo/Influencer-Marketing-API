# Generated by Django 4.1.7 on 2023-08-29 05:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analytics", "0004_promotioncampaign"),
    ]

    operations = [
        migrations.AddField(
            model_name="promotioncampaign",
            name="campaign_url",
            field=models.URLField(max_length=500, null=True),
        ),
    ]
