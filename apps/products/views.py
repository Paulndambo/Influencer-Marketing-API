from django.shortcuts import render

from apps.products.models import Product
from apps.products.serializers import ProductSerializer

from rest_framework.viewsets import ModelViewSet

# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def get_queryset(self):
        ref = self.request.META.items()
        #for key, value in ref:
            #print(f"Key: {key}, Value: {value}")
        return self.queryset

    