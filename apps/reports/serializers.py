from rest_framework import serializers

from apps.analytics.models import Engagement, PromotionCampaign
from apps.products.models import Product


class ProductsReportSerializer(serializers.ModelSerializer):
    total_campaigns = serializers.SerializerMethodField()
    total_engagements = serializers.SerializerMethodField()
    customer_name = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = "__all__"

    def get_total_campaigns(self, obj):
        return obj.productcampaigns.count()

    def get_total_engagements(self, obj):
        return obj.productengagements.count()

    def get_customer_name(self, obj):
        return f"{obj.customer.user.first_name} {obj.customer.user.last_name}"
    