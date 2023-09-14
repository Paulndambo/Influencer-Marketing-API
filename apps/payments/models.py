from django.db import models

from apps.core.models import AbstractBaseModel
from apps.payments.timestamp_to_time import convert_timestamp_to_datetime


# Create your models here.
class Wallet(AbstractBaseModel):
    user = models.OneToOneField("users.User", on_delete=models.CASCADE, related_name="userwallte")
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

class MpesaResponseData(AbstractBaseModel):
    response_data = models.JSONField(default=dict)
    response_description = models.CharField(max_length=1000)
    response_code = models.CharField(max_length=255)

    def __str__(self):
        return self.response_code


class BillingCategory(AbstractBaseModel):
    name = models.CharField(max_length=255)
    charge_per_hour = models.DecimalField(max_digits=10, decimal_places=2)

    
    def __str__(self):
        return f"{self.name} => Charges, ${self.charge_per_hour} Per Hour"


class AdvertisementOrder(AbstractBaseModel):
    product = models.ForeignKey("products.Product", on_delete=models.SET_NULL, null=True)
    advert_package = models.ForeignKey(BillingCategory, on_delete=models.SET_NULL, null=True)
    promotion_period = models.CharField(max_length=255)
    total_bill = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    paid = models.BooleanField(default=False)

    def __str__(self):
        return self.product.name 

    def calculate_promotion_bill(self, period, package_cost, period_in):
        total_bill = 0
        if period_in == "hours":
            total_bill = period * package_cost
        elif period_in == "days":
            total_bill = (period * 24) * package_cost
        elif period_in == "weeks":
            total_bill = (period * 7 * 24) * package_cost
        elif total_bill == "months":
            total_bill = (period * 30 * 24) * package_cost
        
        self.total_bill = total_bill
        self.save()

