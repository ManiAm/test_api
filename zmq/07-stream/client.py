import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.STREAM)

# STREAM sockets require manual management of connection IDs; we'll ignore it for sending
connection_id = socket.connect("tcp://localhost:5555")

# Send a message
message = "Hello, STREAM server!"

# STREAM sockets require sending the connection ID frame first, but for zmq.connect it's managed internally
socket.send(message.encode())
print(f"Sent: {message}")

# Wait a bit for the server to reply
time.sleep(1)

# Receive the echo
_, echo = socket.recv_multipart()
print(f"Received: {echo.decode()}")

socket.close()
context.term()
