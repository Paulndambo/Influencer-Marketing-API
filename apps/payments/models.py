from django.db import models

from apps.core.models import AbstractBaseModel


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
