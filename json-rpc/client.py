from jsonrpclib import Server


def main():

    proxy = Server("http://localhost:4000")

    result = proxy.add(5, 6)
    print(f"Result: {result}")

    # example of an not supported method
    result = proxy.subtract(6, 5)
    print(f"Result: {result}")


if __name__ == '__main__':

    main()
