from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from apps.payments.models import PaymentRecord, Wallet
from apps.payments.serializers import PaymentRecordSerializer, WalletSerializer


# Create your views here.
class WalletViewSet(ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.is_superuser:
            return self.queryset
        return self.queryset.filter(user=user)


class PaymentRecordViewSet(ModelViewSet):
    queryset = PaymentRecord.objects.all()
    serializer_class = PaymentRecordSerializer
    permission_classes = [IsAuthenticated]

   # def get_queryset(self):
    #     user = self.request.user

    #    if user.is_superuser:
    #        return self.queryset
    #    return self.queryset.filter(user=user)
