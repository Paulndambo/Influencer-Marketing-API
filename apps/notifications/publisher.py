import json
import os

import pika

url = os.environ.get('CLOUDAMQ_URL', 'amqps://qiqdvcyl:KPtRQ1jnfpuF7NNuAaVi9tynarNPc6XH@hummingbird.rmq.cloudamqp.com/qiqdvcyl')
params = pika.URLParameters(url)
connection = pika.BlockingConnection(params)
channel = connection.channel()  # Start A Channel

channel.exchange_declare("test_exchange")  # declare an exchange
channel.queue_declare(queue="test_queue")  # Declare Queue
# Create Binding between Queue & Exchange
channel.queue_bind("test_queue", "test_exchange", "tests")

# Publish A Message
channel.basic_publish(
    body=json.dumps({
        "name": "Paul Ndambo",
        "age": 24,
        "school": "Masinde Muliro University of Sci. & Tech.",
        "specialty": "Backend Software Engineering"
    }),
    exchange="test_exchange",
    routing_key="tests"
)
print("Message Sent!.")
channel.close()
connection.close()