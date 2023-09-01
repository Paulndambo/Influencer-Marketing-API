from rest_framework import serializers

from apps.analytics.models import Engagement, PromotionCampaign


class EngagementSerializer(serializers.ModelSerializer):
    product = serializers.SerializerMethodField()

    class Meta:
        model = Engagement
        fields = "__all__"

    def get_product(self, obj):
        return obj.product.name


class PromotionCampaignSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    influencer_name = serializers.SerializerMethodField()

    class Meta:
        model = PromotionCampaign
        fields = "__all__"

    def get_product_name(self, obj):
        return obj.product.name

    def get_influencer_name(self, obj):
        return obj.influencer.user.username
