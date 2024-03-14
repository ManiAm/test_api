import zmq

context = zmq.Context()
socket = context.socket(zmq.STREAM)
socket.bind("tcp://*:5555")

print("STREAM server listening on port 5555...")

while True:

    # First frame is the connection ID, second frame is the data
    connection_id, message = socket.recv_multipart()
    print(f"Received: {message.decode()}")

    # Echo the message back to the client
    socket.send_multipart([connection_id, message])
