from datetime import datetime

from apps.core.publisher import BasePublisher
from apps.products.models import Product
from InfluencerMarketer.celery import app

date_today = datetime.now().date()


@app.task(name="disable_completed_promotions_task")
def disable_completed_promotions_task():
    product_ids = list(Product.objects.filter(
        promotion_ends_on__date=date_today, 
        campaign_limit_reached=False
    ).values_list("id", flat=True))[:100]

    if not product_ids:
        return
        
    publisher = BasePublisher(
        routing_key="check_if_promotion_period_ended",
        body={
            "product_ids": product_ids
        }
    )
    publisher.run()
    