import pika

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

####################

channel.exchange_declare(exchange='altexchange', exchange_type='fanout')

channel.queue_declare(queue='altexchangequeue')
channel.queue_bind('altexchangequeue', 'altexchange')

def alt_queue_on_message_received(ch, method, properties, body):
    print(f'Alt - received new message: {body}')

channel.basic_consume(queue='altexchangequeue', on_message_callback=alt_queue_on_message_received)

####################

channel.exchange_declare(exchange='mainexchange', exchange_type='direct', arguments={'alternate-exchange': 'altexchange'})

channel.queue_declare(queue='mainexchangequeue')
channel.queue_bind('mainexchangequeue', 'mainexchange', 'test')

def main_queue_on_message_received(ch, method, properties, body):
    print(f'Main - received new message: {body}')

channel.basic_consume(queue='mainexchangequeue', on_message_callback=main_queue_on_message_received)

####################

print('Starting Consuming')

channel.start_consuming()
