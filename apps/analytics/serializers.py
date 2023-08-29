from rest_framework import serializers
from apps.analytics.models import Engagement, PromotionCampaign

class EngagementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engagement
        fields = "__all__"


class PromotionCampaignSerializer(serializers.ModelSerializer):
    class Meta:
        model = PromotionCampaign
        fields = "__all__"