from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from apps.users.models import User, Customer, Influencer
from rest_framework.authtoken.models import Token


@receiver(post_save, sender=User)
def create_user_token(sender, instance, created, **kwargs):
    if created:
        Token.objects.create(user=instance)
