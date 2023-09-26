from django.db.models import Q
from rest_framework import status
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from apps.payments.models import AdvertisementOrder
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

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)

        if serializer.is_valid(raise_exception=True):
            #product = Product.objects.create(**data)
            product = serializer.save()

            advert_order = AdvertisementOrder.objects.create(
                product=product,
                advert_package=product.promotion_package,
                promotion_period=f"{product.promotion_period} {product.promotion_period_in}",
            )
            advert_order.calculate_promotion_bill(
                product.promotion_period,
                package_cost=product.promotion_package.charge_per_hour if product.promotion_package else 0,
                period_in=product.promotion_period_in
            )
            #advert_order.save()

            print(f"Product ID: {product.id}")

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_queryset(self):
        user = self.request.user

        if user.is_authenticated:
            if user.role == "customer":
                return self.queryset.filter(customer__user=user)

            elif user.role == "influencer":
                influencer = Influencer.objects.get(user=user)
                influencer_promos = list(influencer.campaigns.values_list("product", flat=True))
                influencer_preferred_platforms = influencer.preferred_platforms
                influencer_preferred_brand_types = influencer.preferred_brand_types
                

                products = self.queryset.exclude(id__in=influencer_promos)


                product_ids = []
                """1. Filter Based on preferred promotion platform"""
                
                for x in products:
                    for y in influencer_preferred_platforms:
                        if y in x.target_platforms:
                            product_ids.append(x.id)

                products_by_platforms = products.filter(id__in=product_ids)

                print(f"Platforms: {products_by_platforms}")
                
                # print(product_preferences)
                """2. Filter based on preferred brands"""
                products_by_brands =  products_by_platforms.filter(brand_type__in=influencer_preferred_brand_types)

                """3. Filter based on minimum followers required to promote"""
                products_by_followers = products_by_brands.filter(min_followers_on_target_platform__lte=int(influencer.average_following))

                """4. Filter based on promotion budget payment"""
                return products_by_followers.filter(promotion_budget_paid=True)
                
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
