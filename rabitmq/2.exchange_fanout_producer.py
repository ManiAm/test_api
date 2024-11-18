import pika

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange='pubsub', exchange_type='fanout')

message = "Hello I want to broadcast this message"

channel.basic_publish(exchange='pubsub', routing_key='', body=message)

print(f"sent message: {message}")

connection.close()
