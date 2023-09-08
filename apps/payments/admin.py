from django.contrib import admin

from apps.payments.models import MpesaTransaction, PaymentRecord, Wallet


# Register your models here.
@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "balance", "withdrawn"]

@admin.register(PaymentRecord)
class PaymentRecordAdmin(admin.ModelAdmin):
    list_display = ["id", "influencer", "product", "amount"]

@admin.register(MpesaTransaction)
class MpesaTransactionAdmin(admin.ModelAdmin):
    list_display = ["product", "PhoneNumber", "MpesaReceiptNumber", "Amount", "TransactionDate"]