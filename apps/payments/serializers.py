from rest_framework import serializers

from apps.payments.models import BillingCategory, PaymentRecord, Wallet


class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields = "__all__"


class PaymentRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentRecord
        fields = "__all__"


class BillingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingCategory
        fields = "__all__"