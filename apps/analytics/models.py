from django.db import models
from apps.core.models import AbstractBaseModel

CHARACTERISTICS_CHOICES = (
    ("clean", "Clean"),
    ("fraudulent", "Fraudulent"),
)


# Create your models here.
class PromotionCampaign(AbstractBaseModel):
    influencer = models.ForeignKey(
        "users.Influencer", on_delete=models.CASCADE, related_name="campaigns"
    )
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="productcampaigns")
    campaign_url = models.URLField(null=True, max_length=500)
    likes = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    influencer_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.influencer.user.username} promoted {self.product.name}"

    def record_engagement(self):
        self.clicks += 1
        self.views += 1
        self.save()


class Engagement(AbstractBaseModel):
    influencer = models.ForeignKey("users.Influencer", on_delete=models.CASCADE)
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    status = models.CharField(
        max_length=255, choices=CHARACTERISTICS_CHOICES, null=True
    )
    customer_ip = models.CharField(max_length=255, null=True)
    device_id = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.influencer.user.username} promoted {self.product.name}"

    def record_views_and_clicks(self):
        self.clicks += 1
        self.views += 1
        self.save()
