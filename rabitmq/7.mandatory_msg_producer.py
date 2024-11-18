import pika
import time

# Setup connection to RabbitMQ server
connection_param = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_param)
channel = connection.channel()

# Declare an exchange (direct type in this case)
exchange_name = 'example_exchange'
channel.exchange_declare(exchange=exchange_name, exchange_type='direct')

# Define a callback for returned messages
def on_message_returned(channel, method, properties, body):
    print(f"Message returned: {body}")

channel.add_on_return_callback(on_message_returned)

for idx in range(100):

    message = f"Mandatory Message {idx}"

    channel.basic_publish(
        exchange=exchange_name,
        routing_key='non_existent_queue',  # Routing key that matches no queue
        body=message,
        mandatory=True
    )

    print(f"Sent message: {message}")

    time.sleep(5)

# Close the connection
connection.close()
