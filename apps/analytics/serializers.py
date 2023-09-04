from rest_framework import serializers

from apps.analytics.models import (Engagement, EngagementComment,
                                   PromotionCampaign)
from apps.core.location_processor import get_customer_location_details
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
        fields = ["text", "customer_ip", "device_id"]


    def create(self, validated_data):
        try:
            campaign_pk = self.context.get("campaign_pk")
            
            text = validated_data.get("text")
            customter_ip = validated_data.get("customer_ip")
            device_id = validated_data.get("device_id")

            reqUrl = f"https://ipapi.co/{customter_ip}/json/"
            
            location = get_customer_location_details(reqUrl)
            country = location.get("country_name")
            city = location.get("city")


            campaign = PromotionCampaign.objects.get(id=campaign_pk)

            campaign.comments += 1
            campaign.save()
            return EngagementComment.objects.create(
                campaign_id=campaign_pk, 
                text=text,
                customer_ip=customter_ip,
                device_id=device_id,
                country=country,
                city=city
            )
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