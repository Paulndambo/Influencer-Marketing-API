from django.urls import path
from . import views
from django.urls import path, include

# from rest_framework_nested.routers import DefaultRouter

from rest_framework_nested import routers
from .views import *


router = routers.DefaultRouter()

router.register("users", views.UserModelViewSet, basename="users")
router.register("customers", views.CustomerViewSet, basename="customers")

router.register("influencers", views.InfluencerViewSet, basename="influencers")

influencers_router = routers.NestedDefaultRouter(
    router, "influencers", lookup="influencer"
)

influencers_router.register(
    "social-profiles", views.InfluencerSocialProfileViewSet, basename="social-profiles"
)
influencers_router.register(
    "work-experiences",
    views.InfluencerWorkExperienceViewSet,
    basename="work-experiences",
)
influencers_router.register(
    "profile-photos", views.InfluencerProfilePhotoViewSet, basename="profile-photos"
)
influencers_router.register(
    "profile-videos", views.InfluencerProfileVideoViewSet, basename="profile-videos"
)


urlpatterns = [
    # path('', views.getRoutes),
    # path("forgot-password/", views.ForgotPasswordAPIView.as_view(), name="forgot_password",),
    # path("change-password/<str:token>/", views.ChangePasswordAPIView.as_view(), name="change_password",),
    path("login/", GetAuthToken.as_view(), name="login"),
    path("register/", RegisterAPI.as_view(), name="register"),
    path("", include(router.urls)),
    path("", include(influencers_router.urls)),
]
