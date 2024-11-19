import pika
import uuid

# Setup connection to RabbitMQ server
connection_param = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_param)
channel = connection.channel()

# Declare a direct exchange
channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

# ----------------------------

# Declare a queue for consuming messages
queue_o = channel.queue_declare(queue='info_queue')

# Bind the queue to the exchange with the routing key 'info'
channel.queue_bind(exchange='direct_logs', queue='info_queue', routing_key='info')

# ----------------------------

queue_name = queue_o.method.queue
cor_id = str(uuid.uuid4())

msg_property = pika.BasicProperties(reply_to=queue_name, correlation_id=cor_id)

msg = "this is a sample message"

# Publish messages with different routing keys
channel.basic_publish(exchange='direct_logs', routing_key='info', body=msg, properties=msg_property)

print(" [x] Sent logs to direct exchange")

# Close the connection
connection.close()
