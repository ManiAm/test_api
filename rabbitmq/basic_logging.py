import pika
import logging

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) -35s %(lineno) -5d: %(message)s')
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)

log = logging.getLogger(__name__)

# Setup connection to RabbitMQ server
connection_param = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_param)
channel = connection.channel()

# Declare an exchange (direct type in this case)
exchange_name = 'example_exchange'
channel.exchange_declare(exchange=exchange_name, exchange_type='direct')

# Define a callback for returned messages
def on_message_returned(channel, method, properties, body):
    log.info(f"Message returned: {body}")

channel.add_on_return_callback(on_message_returned)

for idx in range(100):

    message = f"Mandatory Message {idx}"

    channel.basic_publish(
        exchange=exchange_name,
        routing_key='non_existent_queue',  # Routing key that matches no queue
        body=message,
        mandatory=True
    )

    log.info(f"Sent message: {message}")

    # call this method to handle RabbitMQ events (e.g., messages arriving)
    connection.process_data_events(1)

# Close the connection
connection.close()