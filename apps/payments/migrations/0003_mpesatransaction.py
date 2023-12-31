# Generated by Django 4.2.5 on 2023-09-08 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_wallet'),
    ]

    operations = [
        migrations.CreateModel(
            name='MpesaTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('MerchantRequestID', models.CharField(max_length=255)),
                ('CheckoutRequestID', models.CharField(max_length=255)),
                ('ResultCode', models.IntegerField(default=0)),
                ('ResultDesc', models.CharField(max_length=1000)),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('TransactionDate', models.DateTimeField()),
                ('PhoneNumber', models.CharField(max_length=255)),
                ('MpesaReceiptNumber', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
