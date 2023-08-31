from django.shortcuts import render

from apps.products.models import Product
from apps.users.models import Influencer
from apps.products.serializers import ProductSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly


# Create your views here.
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            if user.role == "customer":
                return self.queryset.filter(customer__user=user)
            elif user.role == "influencer":
                influencer = Influencer.objects.get(user=user)
                influencer_promos = list(
                    influencer.campaigns.values_list("product", flat=True)
                )
                return self.queryset.exclude(id__in=influencer_promos)
                print(influencer_promos)
            # for key, value in ref:
            # print(f"Key: {key}, Value: {value}")
        return self.queryset
