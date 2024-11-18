import pika

# Setup connection to RabbitMQ server
connection_param = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_param)
channel = connection.channel()

channel.exchange_declare(exchange='headersexchange', exchange_type='headers')

channel.queue_declare('letterbox')

bind_args = {
  'x-match': 'any', # 'any' or 'all'
  'name': 'brian',
  'age': '21'
}

channel.queue_bind('letterbox', 'headersexchange', arguments=bind_args)

def on_message_received(ch, method, properties, body):
    print(f'received new message: {body}')

channel.basic_consume(queue='letterbox', auto_ack=True, on_message_callback=on_message_received)

print('Starting Consuming')

channel.start_consuming()
