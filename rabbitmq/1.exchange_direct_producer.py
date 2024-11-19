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

# Publish messages with different routing keys
channel.basic_publish(exchange='direct_logs', routing_key='info', body='Info log')
channel.basic_publish(exchange='direct_logs', routing_key='warning', body='Warning log')
channel.basic_publish(exchange='direct_logs', routing_key='error', body='Error log')
channel.basic_publish(exchange='direct_logs', routing_key='info', body='Info log 2')

print(" [x] Sent logs to direct exchange")

# Close the connection
connection.close()
