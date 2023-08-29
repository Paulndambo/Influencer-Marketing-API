from django.db import models
from apps.core.models import AbstractBaseModel
from django.conf import settings

from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from django.utils.translation import gettext_lazy as _
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser
import uuid

from apps.core.constants import (
    ROLE_CHOICES
)

# Create your models here.
class User(AbstractUser, AbstractBaseModel):
    email = models.EmailField(
        unique=True,
        error_messages={"unique": _("A user with that email already exists.")},
    )
    role = models.CharField(choices=ROLE_CHOICES, max_length=32)


    def __str__(self):
        return f"{self.username} {self.role}"


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
    instagram = models.CharField(max_length=255, null=True)
    tiktok = models.CharField(max_length=255, null=True)
    facebook = models.CharField(max_length=255, null=True)
    twitter = models.CharField(max_length=255, null=True)
    threads = models.CharField(max_length=255, null=True)
    youtube = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.user.username

