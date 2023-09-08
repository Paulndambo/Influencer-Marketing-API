import datetime

from django.contrib.auth import authenticate
from django.db.models import Sum
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.exceptions import AuthenticationFailed

from apps.core.constants import generate_unique_key
from apps.users.models import (Customer, Influencer, InfluencerPreference,
                               InfluencerProfilePhoto, InfluencerProfileVideo,
                               InfluencerWorkExperience, SocialProfile, User)


class AuthTokenCustomSerializer(AuthTokenSerializer):
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        if username and password:
            user = authenticate(username=username, password=password)

            if user:
                if not user.is_active:
                    msg = _("User account is disabled.")
                    raise serializers.ValidationError(
                        msg, code="authorization")
            else:
                msg = _("Unable to log in with provided credentials.")
                raise AuthenticationFailed(msg, code="authorization")
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code="authorization")

        attrs["user"] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "role", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data["username"],
            email=validated_data["email"],
            role=validated_data["role"],
        )
        user.set_password(validated_data["password"])
        user.save()
        return user


class ForgotPasswordSerializer(serializers.Serializer):
    user = None
    email = serializers.EmailField()

    def send_email(self):
        self.user.token = generate_unique_key(self.user.email)
        self.user.token_expiration_date = timezone.now() + timezone.timedelta(hours=24)
        self.user.save()

    def validate_email(self, value):
        try:
            self.user = User.objects.get(email=value)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                "No user found with provided email!")

class ChangePasswordSerializer(serializers.Serializer):
    user = None

    password = serializers.CharField()
    repeat_password = serializers.CharField()

    def save(self, validated_data):
        self.user.set_password(validated_data["password"])
        self.user.token = None
        self.user.token_expiration_date = None
        if not self.user.is_active:
            self.user.activation_date = datetime.date.today()
        self.user.is_active = True
        self.user.save()


    def check_valid_token(self):
        try:
            self.user = User.objects.get(token=self.context["token"])
        except User.DoesNotExist:
            raise serializers.ValidationError("Token is not valid.")
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    #user = serializers.HyperlinkedRelatedField(
    #    view_name='users-detail',
    #    lookup_field='pk',
    #    read_only=True
    #)
    class Meta:
        model = Customer
        fields = "__all__"


class SocialProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialProfile
        fields = "__all__"


class InfluencerWorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfluencerWorkExperience
        fields = "__all__"


class InfluencerProfilePhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfluencerProfilePhoto
        fields = "__all__"


class InfluencerProfileVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfluencerProfileVideo
        fields = "__all__"


class InfluencerSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    comments_collected = serializers.SerializerMethodField()
    likes_collected = serializers.SerializerMethodField()
    total_likes = serializers.SerializerMethodField()
    total_views_collected = serializers.SerializerMethodField()
    total_clicks_collected = serializers.SerializerMethodField()
    total_products_promoted = serializers.SerializerMethodField()
    #promotions = serializers.SerializerMethodField()
    geographic_analysis = serializers.SerializerMethodField()
    clicks_and_views_by_country = serializers.SerializerMethodField()
    clicks_and_views_by_city = serializers.SerializerMethodField()

    class Meta:
        model = Influencer
        fields = "__all__"

    #def get_promotions(self, obj):
    #    return obj.campaigns.values()

    def get_username(self, obj):
        return obj.user.username

    def get_geographic_analysis(self, obj):
        queryset = obj.engagements.values('country', 'city').annotate(
            views_count=Sum('views'),
            clicks_count=Sum('clicks')
        ).order_by('country', 'city')

        return queryset

    def get_clicks_and_views_by_country(self, obj):
        queryset = obj.engagements.values('country').annotate(
            views_count=Sum('views'),
            clicks_count=Sum('clicks')
        ).order_by('country')

        return queryset

    def get_clicks_and_views_by_city(self, obj):
        queryset = obj.engagements.values('city').annotate(
            views_count=Sum('views'),
            clicks_count=Sum('clicks')
        ).order_by('city')

        return queryset


    def get_comments_collected(self, obj):
        return 0
    
    def get_likes_collected(self, obj):
        return obj.engagements.filter(likes=1).count()

    def get_total_likes(self, obj):
        return 0

    def get_total_views_collected(self, obj):
        return obj.engagements.filter(views=1).count()

    def get_total_clicks_collected(self, obj):
        return obj.engagements.filter(clicks=1).count()

    def get_total_products_promoted(self, obj):
        return obj.campaigns.count()


class InfluencerPreferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfluencerPreference
        fields = "__all__"