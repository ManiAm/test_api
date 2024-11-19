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

# ----------------------------

msg_id = 1

while True:

    message = f"messageId={msg_id}"
    channel.basic_publish(exchange='direct_logs', routing_key='info', body=message)
    print(f"send message: {message}")
    wait_time = random.randint(1,4)
    time.sleep(wait_time)
    msg_id += 1
