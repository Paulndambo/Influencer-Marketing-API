from django.urls import include, path
#from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers

from apps.products.views import (ProductCampaignPreferenceViewSet,
                                 ProductViewSet)

router = routers.DefaultRouter()
router.register("", ProductViewSet, basename="products")

products_router = routers.NestedDefaultRouter(router, "", lookup="product")
products_router.register("preferences", ProductCampaignPreferenceViewSet, basename="preferences")

urlpatterns = [
    path("", include(router.urls)),
    path("", include(products_router.urls)),
]
