from datetime import datetime, timedelta

from apps.products.models import Product


def check_if_promotion_period_ended(products: Product):
    try:
        for product in products:
            one_hour_before = product.promotion_ends_on - timedelta(hours=1)
            one_hour_after = product.promotion_ends_on + timedelta(hours=1)

            if one_hour_before <= product.promotion_ends_on <= one_hour_after:
                product.campaign_limit_reached = True
                product.save()
    except Exception as e:
        raise e