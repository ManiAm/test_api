import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5556")

#socket.setsockopt_string(zmq.SUBSCRIBE, "")  # Subscribe to all messages
#socket.setsockopt_string(zmq.SUBSCRIBE, "TopicA")  # Subscribe to TopicA
socket.setsockopt_string(zmq.SUBSCRIBE, "TopicB")  # Subscribe to TopicB

while True:
    message = socket.recv_string()
    print(f"Received update: {message}")
