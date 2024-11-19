import pika

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

# Define the callback function that will be called when a message is received
def callback(ch, method, properties, body):
    print(f" [x] Received {body}")

# Set up the consumer to listen to the queue
channel.basic_consume(queue='info_queue', on_message_callback=callback, auto_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
