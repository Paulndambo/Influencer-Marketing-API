from django.urls import path
from . import views
from django.urls import path, include
from rest_framework_nested.routers import DefaultRouter

from .views import *




router = DefaultRouter()
router.register("users", views.UserModelViewSet, basename="users")



urlpatterns = [
    # path('', views.getRoutes),
    #path("forgot-password/", views.ForgotPasswordAPIView.as_view(), name="forgot_password",),
    #path("change-password/<str:token>/", views.ChangePasswordAPIView.as_view(), name="change_password",),
    path("login/", GetAuthToken.as_view(), name="login"),
    path("register/", RegisterAPI.as_view(), name="register"),
    path("", include(router.urls)),
]