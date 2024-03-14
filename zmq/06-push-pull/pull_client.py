import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://localhost:5557")

while True:
    work = socket.recv_string()
    print(f"Processing {work}")
