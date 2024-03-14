import zmq
import time

context = zmq.Context()
router = context.socket(zmq.ROUTER)
router.bind("tcp://*:5555")

print("ROUTER Server started...")

try:

    while True:
        # Wait for the next request from any client
        client_id, message = router.recv_multipart()
        print(f"Received '{message.decode()}' from client {client_id.decode()}")

        # Send a reply back to the client
        time.sleep(1)  # Simulate some work being done
        reply = f"ACK: {message.decode()}".encode()
        router.send_multipart([client_id, reply])

except KeyboardInterrupt:
    print("Shutting down...")

finally:
    router.close()
    context.term()
