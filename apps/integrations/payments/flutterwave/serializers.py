from rest_framework import serializers


class FlutterWavePaymentPlanSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    interval = serializers.CharField(max_length=255)
    amount = serializers.IntegerField(default=0)
    currency = serializers.CharField(max_length=255)