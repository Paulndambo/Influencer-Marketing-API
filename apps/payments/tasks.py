from apps.core.publisher import BasePublisher
from apps.products.models import Product
from InfluencerMarketer.celery import app


@app.task(name="distribute_promotion_revenue_task")
def distribute_promotion_revenue_task():
    try:
        products_ids = list(Product.objects.filter(revenue_distributed=False,campaign_limit_reached=True).values_list("id", flat=True))

        if not products_ids:
            print("No payments to make found!!")
            return

        publisher = BasePublisher(
            routing_key="calculate_and_distribute_payment",
            body={
                "product_ids": products_ids
            }
        )
        publisher.run()

    except Exception as e:
        raise e