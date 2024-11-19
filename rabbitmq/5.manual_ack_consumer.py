import pika
import time
import random

# Setup connection to RabbitMQ server
connection_param = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_param)
channel = connection.channel()

# Declare a direct exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# ----------------------------

# Declare a queue for consuming messages
channel.queue_declare(queue='info_queue')

# Bind the queue to the exchange with the routing key 'info'
channel.queue_bind(exchange='direct_logs', queue='info_queue', routing_key='info')

channel.basic_qos(prefetch_count=1)

# ----------------------------

# Define the callback function that will be called when a message is received
def callback(ch, method, properties, body):
    processing_time = random.randint(1,6)
    print(f" [x] Received {body}, will take {processing_time} to process")
    time.sleep(processing_time)
    ch.basic_ack(delivery_tag=method.delivery_tag)
    print("Finished processing the message.")

# Set up the consumer to listen to the queue
channel.basic_consume(queue='info_queue', on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
