from rest_framework import serializers

from apps.products.models import Product, ProductCampaignPreference


class ProductSerializer(serializers.ModelSerializer):
    promotion_preferences = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = "__all__"

    def get_promotion_preferences(self, obj):
        return obj.productpreferences.values()


class ProductCampaignPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCampaignPreference
        fields = "__all__"
