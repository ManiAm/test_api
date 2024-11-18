import pika

# Setup connection to RabbitMQ server
connection_param = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_param)
channel = connection.channel()

# Declare a durable queue and bind it to the exchange
exchange_name = 'example_exchange'
queue_name = 'example_queue'
routing_key = 'valid_key'

channel.exchange_declare(exchange=exchange_name, exchange_type='direct')
channel.queue_declare(queue=queue_name, durable=True)
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

# Define a callback to process messages
def callback(ch, method, properties, body):
    print(f"Received message: {body.decode()}")
    ch.basic_ack(delivery_tag=method.delivery_tag)  # Acknowledge the message

channel.basic_consume(queue=queue_name, on_message_callback=callback)

print("Waiting for messages...")
channel.start_consuming()
