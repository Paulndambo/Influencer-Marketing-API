# Generated by Django 4.2.5 on 2023-09-08 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_influencer_minimum_budget_consideration'),
    ]

    operations = [
        migrations.AddField(
            model_name='influencer',
            name='average_following',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
