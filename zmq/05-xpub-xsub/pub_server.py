import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.XPUB)
socket.bind("tcp://*:5556")

print("Publisher started at tcp://*:5556")

try:

    while True:

        # XPUB sockets can receive subscription messages
        # This is a simple example where we just check for any waiting messages
        # and print them, indicating new subscriptions or unsubscriptions
        while socket.get(zmq.EVENTS) & zmq.POLLIN:
            message = socket.recv()
            is_subscription = message[0] == 1
            topic = message[1:].decode()
            if is_subscription:
                print(f"Subscribed to: {topic}")
            else:
                print(f"Unsubscribed from: {topic}")

        # Send a message to all subscribers
        socket.send_string("Hello from XPUB")
        time.sleep(5)

except KeyboardInterrupt:
    print("Publisher shutting down...")

finally:
    socket.close()
    context.term()
