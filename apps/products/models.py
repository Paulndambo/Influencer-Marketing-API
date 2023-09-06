from django.db import models
from django.utils import timezone

from apps.core.models import AbstractBaseModel

current_time = timezone.now()
# Create your models here.
BRAND_TYPES_CHOICES = (
    ("clothes", "Clothes"),
    ("cars", "Cars"),
    ("electronics", "Electronics"),
    ("food", "Food"),
    ("digital_content", "Digital Content"),
    ("houses", "Houses"),
    ("shoes", "Shoes"),
    ("watches", "Watches"),
)

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
    brand_type = models.CharField(max_length=255, null=True, choices=BRAND_TYPES_CHOICES)

    def __str__(self):
        return self.name 

    def save(self, *args, **kwargs) -> None:
        promotion_end_date = current_time + timezone.timedelta(days=self.max_promotion_days)
        self.promotion_ends_on = promotion_end_date
        return super().save(*args, **kwargs)


class ProductCampaignPreference(AbstractBaseModel):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="productpreferences")
    min_targetted_age = models.FloatField(default=1)
    max_targetted_age = models.FloatField(default=250)
    target_platforms = models.CharField(max_length=255, null=True)
    min_followers_on_target_platform = models.IntegerField(default=100)
    min_engagement_percentage = models.FloatField(default=0)

    def __str__(self):
        return self.product.name