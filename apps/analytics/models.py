import uuid

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

    tiktok_url = models.URLField(null=True, max_length=255)
    twitter_url = models.URLField(null=True, max_length=255)
    instagram_url = models.URLField(null=True, max_length=255)
    facebook_url = models.URLField(null=True, max_length=255)
    threads_url = models.URLField(null=True, max_length=255)
    snapchat_url = models.URLField(null=True, max_length=255)
    youtube_url = models.URLField(null=True, max_length=255)
    linkedin_url = models.URLField(null=True, max_length=255)
    
    likes = models.PositiveIntegerField(default=0)
    shares = models.PositiveIntegerField(default=0)
    comments = models.PositiveIntegerField(default=0)
    clicks = models.PositiveIntegerField(default=0)
    views = models.PositiveIntegerField(default=0)
    influencer_paid = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.influencer.user.username} promoted {self.product.name}"

    def record_engagement(self):
        try:
            self.clicks += 1
            self.views += 1
            self.save()
        except Exception as e:
            raise e


class Engagement(AbstractBaseModel):
    influencer = models.ForeignKey("users.Influencer", on_delete=models.CASCADE, related_name="engagements")
    product = models.ForeignKey("products.Product", on_delete=models.CASCADE, related_name="productengagements")
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
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    source = models.CharField(max_length=255, null=True)
    

    def __str__(self):
        return f"{self.influencer.user.username} promoted {self.product.name}"

    def record_views_and_clicks(self):
        """
        When called, the method updates clicks & views on the specific engagement

        Parameters:
        - self: The current engagement object

        Returns:
        - None
        """
        self.clicks += 1
        self.views += 1
        self.save()


class EngagementComment(AbstractBaseModel):
    uuid = models.UUIDField(default=uuid.uuid4())
    campaign = models.ForeignKey(PromotionCampaign, on_delete=models.CASCADE)
    text = models.TextField(null=True)
    customer_ip = models.CharField(max_length=255, null=True)
    device_id = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(uuid)