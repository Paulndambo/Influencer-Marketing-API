from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.analytics.views import (EngagementViewSet, PromotionCampaignViewSet,
                                  ViewsAndClicksAPIView)

router = DefaultRouter()
router.register("engagements", EngagementViewSet, basename="engagements")
router.register(
    "promotion-campaigns", PromotionCampaignViewSet, basename="promotion-campaigns"
)

urlpatterns = [
    path("", include(router.urls)),
    path("views-and-clicks/", ViewsAndClicksAPIView.as_view(), name="views-and-clicks"),
    # path("promote-product/", PromotionCampaignAPIView.as_view(), name="promote-product"),
]
