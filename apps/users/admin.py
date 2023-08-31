from django.contrib import admin
from apps.users.models import User, Customer, Influencer


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "role", "email"]


admin.site.register(Customer)


@admin.register(Influencer)
class InfluencerAdmin(admin.ModelAdmin):
    list_display = ["id", "user", "phone_number"]
