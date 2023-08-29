from django.contrib import admin
from apps.analytics.models import Engagement,PromotionCampaign

# Register your models here.
@admin.register(Engagement)
class EngagementAdmin(admin.ModelAdmin):
    list_display = ["influencer", "product", "views", "clicks", "status", "customer_ip", "device_id"]

admin.site.register(PromotionCampaign)