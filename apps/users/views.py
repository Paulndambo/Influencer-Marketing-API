from django.shortcuts import render
from rest_framework import status, generics, permissions
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser

## Rest Framework Imports
from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from apps.users.models import (
    User, Customer, Influencer, InfluencerProfilePhoto, 
    InfluencerProfileVideo, InfluencerWorkExperience, SocialProfile
)
from apps.users.serializers import (
    UserSerializer, RegisterSerializer, AuthTokenCustomSerializer,
    CustomerSerializer, InfluencerSerializer, InfluencerProfileVideoSerializer,
    InfluencerProfilePhotoSerializer, InfluencerWorkExperienceSerializer, SocialProfileSerializer
)


# Create your views here.
class GetAuthToken(ObtainAuthToken):
    """
    ---
    POST:
        serializer: AuthTokenSerializer
    """
    serializer_class = AuthTokenCustomSerializer
    permission_classes = [AllowAny]

    def get_serializer(self):
        return self.serializer_class()

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token = Token.objects.get(user=user).key

        # Update last_login of the current user
        user.last_login = timezone.now()
        user.save()

        response = {
            "id": user.id,
            'token': token,
            'pk': user.pk,
            'role': user.role,
            "username": user.username,
            "email": user.email,
            "name": f"{user.first_name} {user.last_name}"
            #'view_id': user.get_view_id,
        }

        return Response(response)


class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)


class UserModelViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class InfluencerViewSet(ModelViewSet):
    queryset = Influencer.objects.all()
    serializer_class = InfluencerSerializer


    def get_serializer_context(self):
        return {"request": self.request}


class InfluencerSocialProfileViewSet(ModelViewSet):
    queryset = SocialProfile.objects.all()
    serializer_class = SocialProfileSerializer


    def get_serializer_context(self):
        return {"influencer_pk": self.kwargs.get("influencer_pk")}    

    
    def get_queryset(self):
        influencer_pk = self.kwargs.get("influencer_pk")

        if influencer_pk:
            return self.queryset.filter(influencer_id=influencer_pk)
        return self.queryset


class InfluencerWorkExperienceViewSet(ModelViewSet):
    queryset = InfluencerWorkExperience.objects.all()
    serializer_class = InfluencerWorkExperienceSerializer


    def get_serializer_context(self):
        return {"influencer_pk": self.kwargs.get("influencer_pk")}    


    def get_queryset(self):
        influencer_pk = self.kwargs.get("influencer_pk")

        if influencer_pk:
            return self.queryset.filter(influencer_id=influencer_pk)
        return self.queryset


class InfluencerProfileVideoViewSet(ModelViewSet):
    queryset = InfluencerProfileVideo.objects.all()
    serializer_class = InfluencerProfileVideoSerializer

    def get_serializer_context(self):
        return {"influencer_pk": self.kwargs.get("influencer_pk")}    

    
    def get_queryset(self):
        influencer_pk = self.kwargs.get("influencer_pk")

        if influencer_pk:
            return self.queryset.filter(influencer_id=influencer_pk)
        return self.queryset


class InfluencerProfilePhotoViewSet(ModelViewSet):
    queryset = InfluencerProfilePhoto.objects.all()
    serializer_class = InfluencerProfilePhotoSerializer


    def get_serializer_context(self):
        return {"influencer_pk": self.kwargs.get("influencer_pk")}    

    
    def get_queryset(self):
        influencer_pk = self.kwargs.get("influencer_pk")

        if influencer_pk:
            return self.queryset.filter(influencer_id=influencer_pk)
        return self.queryset