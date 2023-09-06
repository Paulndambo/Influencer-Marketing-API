from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.payments.views import PaymentRecordViewSet, WalletViewSet

router = DefaultRouter()
router.register("wallets", WalletViewSet, basename="wallets")
router.register("payments", PaymentRecordViewSet, basename="payments"
)

urlpatterns = [
    path("", include(router.urls)),
]
