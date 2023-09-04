from django.db import models
from django.utils import timezone

from apps.core.models import AbstractBaseModel

current_time = timezone.now()
# Create your models here.
class Product(AbstractBaseModel):
    name = models.CharField(max_length=255)
    product_url = models.URLField(null=True, max_length=500)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    promotion_budget = models.DecimalField(max_digits=10, decimal_places=2)
    max_promotion_days = models.FloatField(default=1)
    customer = models.ForeignKey("users.Customer", on_delete=models.SET_NULL, null=True)
    campaign_limit_reached = models.BooleanField(default=False)
    revenue_distributed = models.BooleanField(default=False)
    promotion_ends_on = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.customer.user.username}"

    def save(self) -> None:
        promotion_end_date = current_time + timezone.timedelta(days=self.max_promotion_days)
        self.promotion_ends_on = promotion_end_date
        return super().save()
