from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.payments.views import WalletViewSet, PaymentRecordViewSet

router = DefaultRouter()
router.register("wallets", WalletViewSet, basename="wallets")
router.register(
    "influencer-payments", PaymentRecordViewSet, basename="influencer-payments"
)

urlpatterns = [
    path("", include(router.urls)),
]
