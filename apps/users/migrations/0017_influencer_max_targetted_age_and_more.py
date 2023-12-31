# Generated by Django 4.2.5 on 2023-09-08 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_socialprofiledata'),
    ]

    operations = [
        migrations.AddField(
            model_name='influencer',
            name='max_targetted_age',
            field=models.FloatField(default=250),
        ),
        migrations.AddField(
            model_name='influencer',
            name='min_targetted_age',
            field=models.FloatField(default=1),
        ),
        migrations.AddField(
            model_name='influencer',
            name='preferred_brand_types',
            field=models.JSONField(default=list),
        ),
        migrations.AddField(
            model_name='influencer',
            name='preferred_platforms',
            field=models.JSONField(default=list),
        ),
    ]
