import zmq

context = zmq.Context()
socket = context.socket(zmq.XSUB)
socket.connect("tcp://localhost:5556")

print("Connected to the publisher at tcp://localhost:5556")

# Manually subscribing to all messages
# In XSUB, subscription messages start with b"\x01" (subscribe) or b"\x00" (unsubscribe)
# followed by the topic. Here, we subscribe to all topics with b"\x01" + b""
socket.send(b"\x01")

try:

    while True:
        message = socket.recv_string()
        print(f"Received: {message}")

except KeyboardInterrupt:
    print("Subscriber shutting down...")

finally:
    socket.close()
    context.term()
