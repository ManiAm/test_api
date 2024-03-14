import time
import zmq

context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:5557")

# you should run push first!

# waiting for all pull clients to connect
time.sleep(30)

for i in range(100):
    print(f"Sending work {i}")
    socket.send_string(f"Work {i}")
