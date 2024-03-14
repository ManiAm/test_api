import zmq

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.connect("tcp://localhost:5558")

while True:
    message = socket.recv_string()
    print(f"Received {message}")

    socket.send_string("Pong")
