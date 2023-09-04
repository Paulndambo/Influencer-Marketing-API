from django.urls import include, path
#from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from apps.analytics.views import (EngagementCommentViewSet, EngagementViewSet,
                                  PromotionCampaignViewSet,
                                  ViewsAndClicksAPIView)

router = routers.DefaultRouter()

router.register("engagements", EngagementViewSet, basename="engagements")
router.register("campaigns", PromotionCampaignViewSet, basename="campaigns")

campaigns_router = routers.NestedDefaultRouter(router, "campaigns", lookup="campaign")
campaigns_router.register("campaign-comments", EngagementCommentViewSet, basename="campaign-comments")


urlpatterns = [
    path("", include(router.urls)),
    path("views-and-clicks/", ViewsAndClicksAPIView.as_view(), name="views-and-clicks"),
    path("", include(campaigns_router.urls)),
    # path("promote-product/", PromotionCampaignAPIView.as_view(), name="promote-product"),
]
