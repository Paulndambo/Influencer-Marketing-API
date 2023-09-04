
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.core.constants import (JOB_TYPE_CHOICES, ROLE_CHOICES,
                                 WORK_ENVIRONMENT_CHOICES)
from apps.core.models import AbstractBaseModel


# Create your models here.
class User(AbstractUser, AbstractBaseModel):
    email = models.EmailField(
        unique=True,
        error_messages={"unique": _("A user with that email already exists.")},
    )
    role = models.CharField(choices=ROLE_CHOICES, max_length=32)

    def __str__(self):
        return f"{self.username} {self.role}"

    
    def name(self):
        return f"{self.first_name} {self.last_name}"


class Customer(AbstractBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user.username


class Influencer(AbstractBaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", null=True)

    def __str__(self):
        return self.user.username


class InfluencerWorkExperience(AbstractBaseModel):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    employer = models.CharField(max_length=255)
    job_type = models.CharField(max_length=255, choices=JOB_TYPE_CHOICES)
    work_environment = models.CharField(
        max_length=255, choices=WORK_ENVIRONMENT_CHOICES
    )
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.title


class InfluencerProfilePhoto(AbstractBaseModel):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="influencer_photos", null=True)

    def __str__(self):
        return self.influencer.user.username


class InfluencerProfileVideo(AbstractBaseModel):
    influencer = models.ForeignKey(Influencer, on_delete=models.CASCADE)
    video = models.URLField(max_length=1000, null=True)

    def __str__(self):
        return self.influencer.user.username


class SocialProfile(AbstractBaseModel):
    influencer = models.OneToOneField(Influencer, on_delete=models.CASCADE)
    instagram = models.CharField(max_length=255, null=True)
    tiktok = models.CharField(max_length=255, null=True)
    facebook = models.CharField(max_length=255, null=True)
    twitter = models.CharField(max_length=255, null=True)
    threads = models.CharField(max_length=255, null=True)
    youtube = models.CharField(max_length=255, null=True)
    telegram = models.CharField(max_length=255, null=True)
    snapchat = models.CharField(max_length=255, null=True)
    whatsapp_number = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.influencer.user.username
