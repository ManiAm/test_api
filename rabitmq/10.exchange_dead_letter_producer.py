import pika

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange='mainexchange2', exchange_type='direct')

message = 'This message might expire'

channel.basic_publish(exchange='mainexchange2', routing_key='test', body=message)

print(f'sent message: {message}')

connection.close()
