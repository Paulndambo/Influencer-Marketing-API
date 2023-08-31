import os
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from apps.analytics.models import Engagement, PromotionCampaign
from apps.analytics.serializers import EngagementSerializer, PromotionCampaignSerializer
from apps.users.models import Influencer
from apps.products.models import Product
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from apps.analytics.engagement_methods.track_engagement import ViewsAndClicksProcessor

from apps.analytics.engagement_methods.create_engagements import create_engagement

# Create your views here.
current_env = os.environ.get("CURRENT_ENVIRONMENT", "DEVELOPMENT")

BACKEND_URL = "http://127.0.0.1:8000/products"
if current_env == "PRODUCTION":
    BACKEND_URL = "https://influencer-marketing-api.onrender.com/products"


class PromotionCampaignViewSet(ModelViewSet):
    queryset = PromotionCampaign.objects.all()
    serializer_class = PromotionCampaignSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        user = self.request.user

        
        if user.is_authenticated:
            if user.role == "customer":
                return self.queryset.filter(product__customer__user=user)
            elif user.role == "influencer":
                return self.queryset.filter(influencer__user=user)

        return self.queryset

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            product = data.get("product")
            user = data.get("user")

            influencer = Influencer.objects.get(user_id=user)
            campaign_url = f"{BACKEND_URL}/{product}/?ref={influencer.id}"

            campaign_object = {
                "influencer_user_id": user,
                "product_id": product,
                "campaign_url": campaign_url,
            }
            print(campaign_object)

            PromotionCampaign.objects.create(
                influencer=influencer, product_id=product, campaign_url=campaign_url
            )

            return Response(
                {
                    "product": product,
                    "influencer": influencer.user.email,
                    "campaign_url": campaign_url,
                    "environment": current_env,
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            raise e


class EngagementViewSet(ModelViewSet):
    queryset = Engagement.objects.all()
    serializer_class = EngagementSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        if user.role == "customer":
            return self.queryset.filter(product__customer__user=user)
        elif user.role == "influencer":
            return self.queryset.filter(influencer__user=user)

        return self.queryset


class ViewsAndClicksAPIView(APIView):
    def post(self, request):
        try:
            influencer = request.data.get("influencer")
            product = request.data.get("product")
            ip_address = request.data.get("customer_ip")

            device_id = request.data.get("device_id")

            # Check Fraudulent Activity
            existing_engagement = Engagement.objects.filter(
                device_id=device_id, customer_ip=ip_address, product_id=product
            ).first()

            current_campaign = PromotionCampaign.objects.filter(
                product_id=product, influencer_id=influencer
            ).first()

            create_engagement(
                existing_engagement=existing_engagement,
                current_campaign=current_campaign,
                product=product,
                influencer=influencer,
                device_id=device_id,
                ip_address=ip_address,
            )

            return Response(
                {
                    "data": {
                        "influencer": influencer,
                        "product": product,
                        "device_id": device_id,
                    }
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            raise e
