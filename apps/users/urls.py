from django.urls import include, path
from rest_framework_nested import routers

from . import views
from .views import *

router = routers.DefaultRouter()

router.register("users", views.UserModelViewSet, basename="users")
router.register("customers", views.CustomerViewSet, basename="customers")
router.register("influencers", views.InfluencerViewSet, basename="influencers")


# To be able to nest influencer related rquests, we need to create a root influencer router
influencers_router = routers.NestedDefaultRouter(router, "influencers", lookup="influencer")

"""
Below are nested influencer requests endpoints

To use them, the requests will look like;-
    - for social profiles: BASE_URL/influencers/{influencer_pk}/social-profiles/
    - for work experiences: BASE_URL/influencers/{influencer_pk}/work-experiences/
    - for profile photos: BASE_URL/influencers/{influencer_pk}/profile-photos/
    - for profile videos: BASE_URL/influencers/{influencer_pk}/profile-videos/
"""

influencers_router.register("social-profiles", views.InfluencerSocialProfileViewSet, basename="social-profiles")
influencers_router.register("work-experiences", views.InfluencerWorkExperienceViewSet, basename="work-experiences")
influencers_router.register("profile-photos", views.InfluencerProfilePhotoViewSet, basename="profile-photos")
influencers_router.register("profile-videos", views.InfluencerProfileVideoViewSet, basename="profile-videos")


urlpatterns = [
    path("login/", GetAuthToken.as_view(), name="login"),
    path("register/", RegisterAPI.as_view(), name="register"),
    path("", include(router.urls)),
    path("", include(influencers_router.urls)),
]
