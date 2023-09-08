from django.db import models

from apps.core.models import AbstractBaseModel
from apps.payments.timestamp_to_time import convert_timestamp_to_datetime


# Create your models here.
class Wallet(AbstractBaseModel):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE)
    withdrawn = models.DecimalField(max_digits=10, decimal_places=2)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)


class PaymentRecord(AbstractBaseModel):
    influencer = models.ForeignKey("users.Influencer", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.id)


class MpesaTransaction(AbstractBaseModel):
    product = models.ForeignKey("products.Product", on_delete=models.SET_NULL, null=True)
    MerchantRequestID = models.CharField(max_length=255)
    CheckoutRequestID = models.CharField(max_length=255)
    ResultCode = models.IntegerField(default=0)
    ResultDesc = models.CharField(max_length=1000)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    TransactionTimeStamp = models.CharField(max_length=255, null=True)
    TransactionDate = models.DateTimeField()
    PhoneNumber = models.CharField(max_length=255)
    MpesaReceiptNumber = models.CharField(max_length=255)

    def __str__(self):
        return self.MpesaReceiptNumber

    
    def save(self, *args, **kwargs) -> None:
        self.TransactionDate = convert_timestamp_to_datetime(self.TransactionTimeStamp)
        return super().save(*args, **kwargs)