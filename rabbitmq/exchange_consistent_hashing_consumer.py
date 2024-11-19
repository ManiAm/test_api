import pika

connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

channel.exchange_declare(exchange='samplehashing', exchange_type='x-consistent-hash') 

###############################

channel.queue_declare(queue='letterbox1')

channel.queue_bind('letterbox1', 'samplehashing', routing_key='1')

def callback_1(ch, method, properties, body):
    print(f'queue 1 received new message: {body}')

channel.basic_consume(queue='letterbox1', auto_ack=True, on_message_callback=callback_1)

###############################

channel.queue_declare(queue='letterbox2')

channel.queue_bind('letterbox2', 'samplehashing', routing_key='2')

def callback_2(ch, method, properties, body):
    print(f'queue 2 received new message: {body}')

channel.basic_consume(queue='letterbox2', auto_ack=True, on_message_callback=callback_2)

###############################

print('Starting Consuming')

channel.start_consuming()
