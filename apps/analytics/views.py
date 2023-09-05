import os

import requests
from rest_framework import generics, status
from rest_framework.permissions import (IsAuthenticated,
                                        IsAuthenticatedOrReadOnly)
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from apps.analytics.engagement_methods.create_engagements import \
    create_engagement
from apps.analytics.models import (Engagement, EngagementComment,
                                   PromotionCampaign)
from apps.analytics.serializers import (EngagementCommentCreateSerializer,
                                        EngagementCommentSerializer,
                                        EngagementSerializer,
                                        InfluencerAnalyticsSerializer,
                                        PromotionCampaignSerializer)
from apps.core.location_processor import get_customer_location_details
from apps.core.utm_constructor import utm_constructor
from apps.products.models import Product
from apps.users.models import Influencer

# Create your views here.
current_env = os.environ.get("CURRENT_ENVIRONMENT", "DEVELOPMENT")

BACKEND_URL = "http://127.0.0.1:3000/products"
if current_env == "PRODUCTION":
    BACKEND_URL = "https://influencer-marketing-api.onrender.com/products"


class PromotionCampaignViewSet(ModelViewSet):
    """
    Description:
    - This view is used by influencers to create product campaigns on their socials.

    Parameters:
    1. POST
        - product: The product being promoted on the campaign.
        - user: The current user, who is the influencer promoting the product.

    Returns:
    - json_data: A response based on current user;-
        - if influencer, returns only campaigns posted by them.
        - if customer, returns only campaigns related to their products.
        - if admin, returns all campaigns.
    """

    queryset = PromotionCampaign.objects.all()
    serializer_class = PromotionCampaignSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_context(self):
        return {"request": self.request}

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
            product_id = data.get("product")
            user = data.get("user")

            influencer = Influencer.objects.get(user_id=user)
            product = Product.objects.get(id=product_id)
            #campaign_url = f"{BACKEND_URL}/{product}/?ref={influencer.id}"

            product_url = f"{BACKEND_URL}/{product.id}/"

            tiktok_url, facebook_url, twitter_url, instagram_url, youtube_url, threads_url, email_url, snapchat_url, linkedin_url = utm_constructor(
                product_url, product.id, influencer.id)

            PromotionCampaign.objects.create(
                influencer=influencer,
                product=product,
                campaign_url=product_url,
                tiktok_url=tiktok_url,
                twitter_url=twitter_url,
                threads_url=threads_url,
                instagram_url=instagram_url,
                snapchat_url=snapchat_url,
                youtube_url=youtube_url,
                facebook_url=facebook_url,
                linkedin_url=linkedin_url,
                email_url=email_url
            )

            return Response(
                {
                    "product": product.id,
                    "influencer": influencer.user.email,
                    "campaign_url": product_url,
                    "environment": current_env,
                    "tiktok_url": tiktok_url,
                    "twitter_url": twitter_url,
                    "threads_url": threads_url,
                    "instagram_url": instagram_url,
                    "snapchat_url": snapchat_url,
                    "youtube_url": youtube_url,
                    "facebook_url": facebook_url,
                    "linkedin_url": linkedin_url,
                    "email_url": email_url
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            raise e


class EngagementViewSet(ModelViewSet):
    """
    Description:
    - This view is not really used for any post, patch, put or delete for now
        - In this case it is only used to get

    Parameters:
    - None

    Returns:
    - json_data: Enagegement data based on current user;-
        - if current user is an influencer, returns engagement data on campaigns posted.
        - if current user is customer, returns engagement data on campaigns for their products.
        - if current user is admin, returns all the data 
    """

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
    """
    Description:
    - Reads user activity on promoted products.

    Parameters:
    - influencer: The reference of the influencer who promoted the product.
    - product: The reference to the product being promoted by influencers.
    - customer_ip: The ip address of the customer who has viewed/clicked a promoted product.
    - device_id: The device id of the customer who has viewed/clicked a promoted product.

    Returns:
    - json_data: dict object, {"influencer": , "product": , "customer_ip": , "device_id": }

    """

    def post(self, request):
        try:
            #influencer = request.data.get("influencer")
            #product = request.data.get("product")
            campaign = str(request.data.get("utm_campaign"))
            ip_address = request.data.get("customer_ip")
            device_id = request.data.get("device_id")
            source = request.data.get("utm_source")

            campaign_items = campaign.split("-")
            product = int(campaign_items[0])
            influencer = int(campaign_items[1])


            reqUrl = f"https://ipapi.co/{ip_address}/json/"

            location = get_customer_location_details(reqUrl)
            country = location.get("country_name")
            city = location.get("city")

            # Check Fraudulent Activity
            # Same IP, Device ID and Product on multiple records will be flagged as fraud

            # existing_engagement = Engagement.objects.filter(
            #    device_id=device_id, customer_ip=ip_address, product_id=product
            # ).first()

            # This gets the specific campaign posted by the influencer on the product
            # current_campaign = PromotionCampaign.objects.filter(
            #    product_id=product, influencer_id=influencer
            # ).first()
            params = request.query_params
            print(f"Query Params: {params}")

            """
            create_engagement(
                existing_engagement=existing_engagement,
                current_campaign=current_campaign,
                product=product,
                influencer=influencer,
                device_id=device_id,
                ip_address=ip_address,
                country=country,
                city=city,
                source=source
            )
            """

            return Response(
                {
                    "data": {
                        "influencer": influencer,
                        "product": product,
                        "device_id": device_id,
                        "location": {
                            "country": country,
                            "city": city
                        },
                        "source": source
                    }
                },
                status=status.HTTP_201_CREATED,
            )
        except Exception as e:
            raise e


class EngagementCommentViewSet(ModelViewSet):
    queryset = EngagementComment.objects.all()
    serializer_class = EngagementCommentSerializer

    def get_serializer_context(self):
        return {"campaign_pk": self.kwargs.get("campaign_pk")}

    def get_serializer_class(self):
        if self.request.method == "POST":
            return EngagementCommentCreateSerializer
        return EngagementCommentSerializer


class InfluencerAnalyticsAPIView(generics.ListAPIView):
    queryset = Influencer.objects.all()
    serializer_class = InfluencerAnalyticsSerializer
