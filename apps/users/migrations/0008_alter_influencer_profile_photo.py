# Generated by Django 4.1.7 on 2023-08-31 06:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0007_influencerworkexperience"),
    ]

    operations = [
        migrations.AlterField(
            model_name="influencer",
            name="profile_photo",
            field=models.ImageField(null=True, upload_to="influencer_profile_photos/"),
        ),
    ]
