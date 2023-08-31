from datetime import datetime, timedelta
from django.utils import timezone

from apps.products.models import Product

date_today = datetime.now().now()
current_time = timezone.now()
two_hours_ago = timezone.now() - timezone.timedelta(hours=2)

def check_if_promotion_period_ended():
    products = Product.objects.filter(campaign_limit_reached=False)

    if not products:
        return

    for product in products:
        one_hour_before = product.promotion_ends_on - timedelta(hours=1)
        one_hour_after = product.promotion_ends_on + timedelta(hours=1)

        if one_hour_before <= product.promotion_ends_on <= one_hour_after:
            product.campaign_limit_reached = True
            product.save()