from apps.core.publisher import BasePublisher
from InfluencerMarketer.celery import app


@app.task(name="print_hello_world")
def print_hello_world():
    
    publisher = BasePublisher(
        routing_key="hello_world",
        body={
            "text": "The publisher is up and running!!"
        }
    )
    publisher.run()
    
    print("**************Hello World***************")
