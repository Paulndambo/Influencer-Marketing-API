import os

from celery import Celery
from django.conf import settings

cloud_amqp = "amqps://qiqdvcyl:KPtRQ1jnfpuF7NNuAaVi9tynarNPc6XH@hummingbird.rmq.cloudamqp.com/qiqdvcyl"
#cloud_amqp = "amqp//guest:guest@rabbitmq:5672/"
DOCKER_COMPOSE_MQ = "amqp://admin:admin@rabbitmq"

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "InfluencerMarketer.settings")

app = Celery("InfluencerMarketer", broker=cloud_amqp)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()