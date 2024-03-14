import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:5556")

while True:

        # "topic" is the prefix of the message

        socket.send_string("TopicA Message from Topic A")
        print("Sent a message on TopicA")

        socket.send_string("TopicB Message from Topic B")
        print("Sent a message on TopicB")

        time.sleep(1)
