import pika

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type='fanout')

# ----------------------------

# queue='': server will choose a random queue name
# exclusive=true: once the consumer connection is closed, the queue is deleted
queue = channel.queue_declare(queue='', exclusive=True)

queue_name = queue.method.queue
print(f"queue_name is {queue_name}")

channel.queue_bind(exchange='pubsub', queue=queue_name)

# ----------------------------

def callback(ch, method, properties, body):
    print(f"secondconsumer - received new message: {body}")

channel.basic_consume(queue=queue_name, auto_ack=True, on_message_callback=callback)

print("Starting Consuming")

channel.start_consuming()
