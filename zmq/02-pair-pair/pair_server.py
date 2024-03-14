import zmq

context = zmq.Context()
socket = context.socket(zmq.PAIR)
socket.bind("tcp://*:5558")

while True:
    socket.send_string("Ping")

    message = socket.recv_string()
    print(f"Received {message}")
