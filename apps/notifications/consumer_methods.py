import json
from decimal import Decimal

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
                product.campaign_limit_reached = True
                product.save()

            except Exception as e:
                raise e
