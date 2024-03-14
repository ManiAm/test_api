from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer


def add(x, y):
    """A simple function that adds two numbers."""

    return x + y


def main():

    server = SimpleJSONRPCServer(('localhost', 4000))
    server.register_function(add, 'add')

    print("Starting server on localhost:4000")
    server.serve_forever()


if __name__ == '__main__':

    main()
