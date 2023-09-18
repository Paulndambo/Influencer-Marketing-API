import requests
from rest_framework import generics, status
from rest_framework.response import Response

FLUTERWAVE_BACKEND_URL = "https://api.flutterwave.com/v3/payment-plans"

from apps.integrations.payments.flutterwave.flutterwave_processor import \
    FluterWavePaymentProcessor
from apps.integrations.payments.flutterwave.serializers import \
    FlutterWavePaymentPlanSerializer


class FlutterWavePaymentPlanAPIView(generics.ListCreateAPIView):
    serializer_class = FlutterWavePaymentPlanSerializer

    def get(self, request):
        flutterwave = FluterWavePaymentProcessor()
        pps = flutterwave.get_payment_plans()
        return Response(pps)

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            name = serializer.validated_data.get("name")
            currency = serializer.validated_data.get("currency")
            amount = serializer.validated_data.get("amount")
            interval = serializer.validated_data.get("interval")
            try:
                flutterwave = FluterWavePaymentProcessor()
                res = flutterwave.create_payment_plan(name, amount, currency, interval)
                return Response(res, status=status.HTTP_200_OK)
            except Exception as e:
                raise e

            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)