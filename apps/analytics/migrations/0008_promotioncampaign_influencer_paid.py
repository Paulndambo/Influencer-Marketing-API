# Generated by Django 4.1.7 on 2023-08-31 08:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("analytics", "0007_alter_promotioncampaign_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="promotioncampaign",
            name="influencer_paid",
            field=models.BooleanField(default=False),
        ),
    ]
