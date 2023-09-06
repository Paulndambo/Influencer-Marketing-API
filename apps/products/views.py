from django.db.models import Q
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.viewsets import ModelViewSet

from apps.products.models import Product, ProductCampaignPreference
from apps.products.serializers import (ProductCampaignPreferenceSerializer,
                                       ProductSerializer)
from apps.users.models import Influencer


# Create your views here.
class ProductViewSet(ModelViewSet):
    """
    Description:
    - This view is reponsible for;-
        - fetching products and returning to the user.
        - creating, edit, and deleting products.

    Parameters:
    - None.

    Returns:
    - json_data: Response data based on the current user.
        - if not logged in, the user will see all posted products.
        - if user is customer, they will see all the products they have posted.
        - if user is influencer, they will see all products which they have not promoted yet.
        - if user is admin, will see all the products.

    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        return {"request": self.request}
        

    def get_queryset(self):
        user = self.request.user
        

        if user.is_authenticated:
            if user.role == "customer":
                return self.queryset.filter(customer__user=user)


            elif user.role == "influencer":
                influencer = Influencer.objects.get(user=user)
                influencer_promos = list(influencer.campaigns.values_list("product", flat=True))

                products = self.queryset.exclude(id__in=influencer_promos)

                influencer_preferences = list(influencer.influencerpreferences.values_list('preferred_platforms', flat=True))[0]
                influencer_preferred_brand_types = list(influencer.influencerpreferences.values_list('preferred_brand_types', flat=True))[0]
                product_preferences = ProductCampaignPreference.objects.filter(product__in=products)

                product_ids = []

                """1. Filter Based on preferred promotion platform"""

                for x in product_preferences:
                    for y in influencer_preferences:
                        if y in x.target_platforms:
                            product_ids.append(x.product.id)


                products_by_platform_pref = products.filter(id__in=product_ids)
                
                #print(product_preferences)
                """2. Filter based on preferred brands"""
                return products_by_platform_pref.filter(brand_type__in=influencer_preferred_brand_types)


        return self.queryset


class ProductCampaignPreferenceViewSet(ModelViewSet):
    queryset = ProductCampaignPreference.objects.all()
    serializer_class = ProductCampaignPreferenceSerializer

    def get_serializer_context(self):
        return {"product_pk": self.kwargs.get("product_pk")}

    def get_queryset(self):
        product_pk = self.kwargs.get("product_pk")
        if product_pk:
            return self.queryset.filter(product_id=product_pk)
        return self.queryset