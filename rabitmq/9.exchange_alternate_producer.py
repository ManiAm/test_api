import pika

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

####################

channel.exchange_declare(exchange='altexchange', exchange_type='fanout')

channel.exchange_declare(exchange='mainexchange', exchange_type='direct', arguments={'alternate-exchange': 'altexchange'})

message = 'msg goes to main'
channel.basic_publish(exchange='mainexchange', routing_key='test', body=message)

message = 'msg goes to alternate'
channel.basic_publish(exchange='mainexchange', routing_key='test_1', body=message)

print(f'sent message: {message}')

connection.close()
