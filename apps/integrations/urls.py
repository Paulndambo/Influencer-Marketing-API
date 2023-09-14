from django.urls import path

from apps.integrations.payments.manual.manual_payment import \
    ManualPaymentAPIView
from apps.integrations.payments.mpesa.mpesa import (LipaNaMpesaAPIView,
                                                    LipaNaMpesaCallbackAPIView)

urlpatterns = [
    path("lipa-na-mpesa/", LipaNaMpesaAPIView.as_view(), name="lipa-na-mpesa"),
    path("lipa-na-mpesa-callback/", LipaNaMpesaCallbackAPIView.as_view(), name="lipa-na-mpesa-callback"),
    path("manual-payment/", ManualPaymentAPIView.as_view(), name="manual-payment"),
]