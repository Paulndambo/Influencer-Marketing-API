from django.db import models
from apps.core.models import AbstractBaseModel
# Create your models here.
class Product(AbstractBaseModel):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    promotion_budget = models.DecimalField(max_digits=10, decimal_places=2)
    max_promotion_days = models.FloatField(default=1)
    customer = models.ForeignKey("users.Customer", on_delete=models.SET_NULL, null=True)
    campaign_limit_reached = models.BooleanField(default=False)

    def __str__(self):
        return self.name