import pika

# Setup connection to RabbitMQ server
connection_param = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_param)
channel = connection.channel()

# Enable Publisher Confirms
channel.confirm_delivery()

#######################################

exchange_name = 'example_exchange'
queue_name = 'my_example_queue'
routing_key = 'valid_key'

channel.exchange_declare(exchange=exchange_name, exchange_type='direct')
channel.queue_declare(queue=queue_name)
channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)

try:

    channel.basic_publish(
        exchange='example_exchange',
        routing_key='non_existent_queue',  # Routing key matches no queue
        body='Message without mandatory flag'
    )

    print("Message was acknowledged by the broker.")

except pika.exceptions.NackError:

    print("Message was not acknowledged (nacked).")

#######################################

connection.close()
