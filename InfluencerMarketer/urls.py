from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("payments/", include("apps.payments.urls")),
    path("users/", include("apps.users.urls")),
    path("products/", include("apps.products.urls")),
    path("analytics/", include("apps.analytics.urls")),
]
