import pika

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

###############################

channel.exchange_declare(exchange='dlx', exchange_type='fanout')
channel.queue_declare('deadletterqueue')
channel.queue_bind('deadletterqueue', 'dlx')

def deadletter_queue_on_message_received(ch, method, properties, body):
    print(f'Dead letter - received new message: {body}')
    ch.basic_ack(method.delivery_tag)

channel.basic_consume(queue='deadletterqueue', on_message_callback=deadletter_queue_on_message_received)

###############################

channel.exchange_declare(exchange='mainexchange2', exchange_type='direct')
channel.queue_declare(queue='mainexchangequeue2', arguments={'x-dead-letter-exchange': 'dlx',  'x-message-ttl': 5000})
channel.queue_bind('mainexchangequeue2', 'mainexchange2', routing_key='test')

def main_queue_on_message_received(ch, method, properties, body):
    print(f'Main - received new message: {body}')

# commented so that no messages are consumed from 'mainexchangequeue2' queue
#channel.basic_consume(queue='mainexchangequeue2', on_message_callback=main_queue_on_message_received)

###############################

print('Starting Consuming')

channel.start_consuming()
