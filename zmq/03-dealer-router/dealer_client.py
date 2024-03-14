import zmq
import time
import random

client_id = random.randint(10000, 99999)
client_id = str(client_id)

context = zmq.Context()
dealer = context.socket(zmq.DEALER)
dealer.setsockopt_string(zmq.IDENTITY, client_id)
dealer.connect("tcp://localhost:5555")

print(f"DEALER Client {client_id} started...")

messages = ["Hello", "How are you?", "Goodbye"]
for msg in messages:
    print(f"Client {client_id} sending: {msg}")
    dealer.send_string(msg)
    time.sleep(1)

for _ in messages:
    reply = dealer.recv()
    print(f"Client {client_id} received reply: {reply.decode()}")

dealer.close()
context.term()
