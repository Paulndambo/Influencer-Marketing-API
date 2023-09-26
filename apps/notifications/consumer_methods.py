import json
from datetime import timedelta

from apps.payments.distribute_promotion_budget import \
    distribute_promotion_budget
from apps.products.models import Product


class NotificationConsumer:
    body = None

    @classmethod
    def hello_world(cls):
        print(cls.body)

    @classmethod
    def calculate_and_distribute_payment(cls):
        product_ids = json.loads(cls.body)['product_ids']
        print(f"Product IDs: {product_ids}")

        products = Product.objects.filter(id__in=product_ids)

        for product in products:
            try:
                distribute_promotion_budget(product)
                product.revenue_distributed = True
                product.save()

            except Exception as e:
                raise e

    @classmethod
    def check_if_promotion_period_ended(cls):
        product_ids = json.loads(cls.body)["product_ids"]
        print(f"Product IDs: {product_ids}")
        products = Product.objects.filter(id__in=product_ids)
        try:
            for product in products:
                one_hour_before = product.promotion_ends_on - \
                    timedelta(hours=1)
                one_hour_after = product.promotion_ends_on + timedelta(hours=1)

                if one_hour_before <= product.promotion_ends_on <= one_hour_after:
                    product.campaign_limit_reached = True
                    product.save()
        except Exception as e:
            raise e
