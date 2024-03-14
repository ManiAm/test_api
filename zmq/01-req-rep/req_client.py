import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

print("Sending request")
socket.send_string("Hello")

message = socket.recv_string()
print(f"Received reply: {message}")
