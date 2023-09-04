from django.contrib import admin

from apps.analytics.models import (Engagement, EngagementComment,
                                   PromotionCampaign)


# Register your models here.
@admin.register(Engagement)
class EngagementAdmin(admin.ModelAdmin):
    list_display = [
        "influencer",
        "product",
        "views",
        "clicks",
        "status",
        "customer_ip",
        "device_id",
        "city",
        "country"
    ]


@admin.register(EngagementComment)
class EngagementCommentAdmin(admin.ModelAdmin):
    list_display = ["uuid", "campaign", "text"]

@admin.register(PromotionCampaign)
class PromotionCampaignAdmin(admin.ModelAdmin):
    list_display = ["product", "influencer", "campaign_url", "likes", "views", "influencer_paid"]
