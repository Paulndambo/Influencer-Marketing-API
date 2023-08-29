from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics

from apps.analytics.models import Engagement, PromotionCampaign
from apps.analytics.serializers import EngagementSerializer, PromotionCampaignSerializer
from apps.users.models import Influencer
from apps.products.models import Product

from apps.analytics.engagement_methods.track_engagement import ViewsAndClicksProcessor
# Create your views here.
BACKEND_URL = "http://127.0.0.1:8000/products"


class PromotionCampaignViewSet(ModelViewSet):
    queryset = PromotionCampaign.objects.all()
    serializer_class = PromotionCampaignSerializer

    def create(self, request, *args, **kwargs):
        try:
            data = request.data
            product = data.get("product")
            influencer = data.get("influencer")

            campaign_url = f"{BACKEND_URL}/{product}/?ref={influencer}"

            PromotionCampaign.objects.create(
                influencer_id=influencer,
                product_id=product,
                campaign_url=campaign_url
            )

            return Response({
                "product": product,
                "influencer": influencer,
                "campaign_url": campaign_url
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            raise e




class EngagementViewSet(ModelViewSet):
    queryset = Engagement.objects.all()
    serializer_class = EngagementSerializer


class ViewsAndClicksAPIView(APIView):

    def get_client_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip


    def post(self, request):
        influencer = request.data.get('influencer')
        product = request.data.get('product')
        ip_address = request.data.get('customer_ip')

        device_id = request.data.get('device_id')
        
        engagement = Engagement.objects.create(
            product_id=product, 
            influencer_id=influencer,
            device_id=device_id,
            customer_ip=ip_address
        )

        engagement.record_views_and_clicks()
    

        return Response({"data": {
            "influencer": influencer,
            "product": product,
            "device_id": device_id,
        }}, status=status.HTTP_201_CREATED)
