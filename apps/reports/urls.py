from django.urls import path

from apps.reports.views import ProductReportAPIView

urlpatterns = [
    path("product-reports/", ProductReportAPIView.as_view(), name="product-reports"),
]