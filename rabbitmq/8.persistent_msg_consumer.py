import pika

# Setup connection to RabbitMQ server
connection_param = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_param)
channel = connection.channel()

# Declare the same durable queue (to ensure it exists)
queue_name = 'persistent_queue'
channel.queue_declare(queue=queue_name, durable=True)

# Define a callback to process messages
def callback(ch, method, properties, body):
    print(f"Received: {body.decode()}")
    # Acknowledge the message to remove it from the queue
    ch.basic_ack(delivery_tag=method.delivery_tag)

# Start consuming messages
channel.basic_consume(queue=queue_name, on_message_callback=callback)
print("Waiting for messages. To exit, press CTRL+C")
channel.start_consuming()
