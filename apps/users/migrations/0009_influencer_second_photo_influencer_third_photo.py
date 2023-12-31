# Generated by Django 4.1.7 on 2023-08-31 06:07

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0008_alter_influencer_profile_photo"),
    ]

    operations = [
        migrations.AddField(
            model_name="influencer",
            name="second_photo",
            field=models.ImageField(null=True, upload_to="profile_images/"),
        ),
        migrations.AddField(
            model_name="influencer",
            name="third_photo",
            field=models.FileField(null=True, upload_to="profile_images/"),
        ),
    ]
