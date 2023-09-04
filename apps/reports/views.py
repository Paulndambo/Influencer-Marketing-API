from rest_framework import generics, status
from rest_framework.response import Response

from apps.products.models import Product
from apps.reports.custom_pagination import CustomPagination
from apps.reports.serializers import ProductsReportSerializer


# Create your views here.
class ProductReportAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsReportSerializer
    
    pagination_class = CustomPagination