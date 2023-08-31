from apps.payments.distribute_promotion_budget import \
    calculate_and_distribute_payment
from apps.products.models import Product
from InfluencerMarketer.celery import app


@app.task(name="distribute_promotion_revenue_task")
def distribute_promotion_revenue_task():
    try:
        products = Product.objects.filter(revenue_distributed=False,campaign_limit_reached=True)[:10]

        if not products:
            print("No payments to make found!!")
            return

        for product in products:
            calculate_and_distribute_payment(product)

    except Exception as e:
        raise e