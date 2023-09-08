from django.urls import path

from apps.integrations.payments.manual.manual_payment import \
    ManualPaymentAPIView
from apps.integrations.payments.mpesa.mpesa import LipaNaMpesaAPIView

urlpatterns = [
    path("lipa-na-mpesa/", LipaNaMpesaAPIView.as_view(), name="lipa-na-mpesa"),
    path("manual-payment/", ManualPaymentAPIView.as_view(), name="manual-payment"),
]