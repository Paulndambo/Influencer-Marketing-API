from django.contrib import admin

from apps.payments.models import (AdvertisementOrder, BillingCategory,
                                  MpesaResponseData, MpesaTransaction,
                                  PaymentRecord, Wallet)


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


@admin.register(MpesaResponseData)
class MpesaResponseDataAdmin(admin.ModelAdmin):
    list_display = ["response_data", "response_description", "response_code"]


@admin.register(BillingCategory)
class BillingCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "charge_per_hour"]


@admin.register(AdvertisementOrder)
class AdvertisementOrderAdmin(admin.ModelAdmin):
    list_display = ["product", "advert_package", "promotion_period", "total_bill", "paid"]