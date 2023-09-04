from rest_framework import serializers

from apps.analytics.models import (Engagement, EngagementComment,
                                   PromotionCampaign)
from apps.users.models import Influencer


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


class EngagementCommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementComment
        fields = ["text"]


    def create(self, validated_data):
        try:
            campaign_pk = self.context.get("campaign_pk")
            text = validated_data.get("text")
            campaign = PromotionCampaign.objects.get(id=campaign_pk)
            campaign.comments += 1
            campaign.save()
            return EngagementComment.objects.create(campaign_id=campaign_pk, text=text)
        except Exception as e:
            raise e
       

class EngagementCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = EngagementComment
        fields = "__all__"


class InfluencerAnalyticsSerializer(serializers.ModelSerializer):
    comments_collected = serializers.SerializerMethodField()
    likes_collected = serializers.SerializerMethodField()
    total_likes = serializers.SerializerMethodField()
    total_views_collected = serializers.SerializerMethodField()
    total_products_promoted = serializers.SerializerMethodField()
    promotions = serializers.SerializerMethodField()

    class Meta:
        model = Influencer
        fields = "__all__"

    def get_promotions(self, obj):
        return obj.campaigns.values()

    def get_comments_collected(self, obj):
        return 0
    
    def get_likes_collected(self, obj):
        return 0

    def get_total_likes(self, obj):
        return 0

    def get_total_views_collected(self, obj):
        return 0

    def get_total_products_promoted(self, obj):
        return 0