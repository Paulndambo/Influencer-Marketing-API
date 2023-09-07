
from InfluencerMarketer.celery import app


@app.task(name="print_hello_world")
def print_hello_world():
    print("**************Hello World***************")


app.conf.beat_schedule = {
    "run-every-2-seconds": {"task": "print_hello_world", "schedule": 2},
    "run-every-5-seconds": {"task": "distribute_promotion_revenue_task", "schedule": 5},
    "run-every-10-seconds": {"task": "disable_completed_promotions_task", "schedule": 10}
}