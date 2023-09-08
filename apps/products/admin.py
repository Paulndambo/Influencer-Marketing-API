from django.contrib import admin

from .models import Product, ProductCampaignPreference


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "name",
        "price",
        "customer",
        "promotion_ends_on",
        "target_platforms",
        "promotion_budget_paid"
    ]

@admin.register(ProductCampaignPreference)
class ProductCampaignPreferenceAdmin(admin.ModelAdmin):
    list_display = ["product", "target_platforms"]