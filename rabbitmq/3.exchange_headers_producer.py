import pika

# Setup connection to RabbitMQ server
connection_param = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_param)
channel = connection.channel()

channel.exchange_declare(exchange='headersexchange', exchange_type='headers')

message = 'This message will be sent with headers'

channel.basic_publish(
    exchange='headersexchange', 
    routing_key='', 
    body=message, 
    properties=pika.BasicProperties(headers={'name': 'brian'}))

print(f'sent message: {message}')

connection.close()
