# Generated by Django 4.1.7 on 2023-08-28 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='engagement',
            name='status',
            field=models.CharField(choices=[('clean', 'Clean'), ('fraudulent', 'Fraudulent')], max_length=255, null=True),
        ),
    ]
