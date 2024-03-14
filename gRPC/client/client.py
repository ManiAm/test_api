import os
import sys
import grpc

# Add the 'generated' directory to the Python path
sys.path.append(os.path.abspath('./generated'))

import helloworld_pb2
import helloworld_pb2_grpc

def run():

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = helloworld_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(helloworld_pb2.HelloRequest(name='world'))
        print("Greeter client received: " + response.message)


if __name__ == '__main__':

    run()
