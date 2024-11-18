import pika

# Setup connection to RabbitMQ server
connection_param = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_param)
channel = connection.channel()

# Declare a durable queue and mark it durable
queue_name = 'persistent_queue'
channel.queue_declare(queue=queue_name, durable=True)

# Publish persistent messages
for idx in range(5):

    message = f"Persistent Message {idx}"

    channel.basic_publish(
        exchange='',  # Default exchange
        routing_key=queue_name,
        body=message,
        properties=pika.BasicProperties(delivery_mode=2)  # Mark message as persistent
    )

    print(f"Sent: {message}")

# Close the connection
connection.close()
