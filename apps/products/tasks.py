from apps.products.models import Product
from apps.products.promotion_tracking import check_if_promotion_period_ended
from InfluencerMarketer.celery import app


@app.task(name="disable_completed_promotions_task")
def disable_completed_promotions_task():
    products = Product.objects.filter(campaign_limit_reached=False)

    if not products:
        return
        
    check_if_promotion_period_ended(products)