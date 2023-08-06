import socket

def main():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Server address and port
    server_address = ('localhost', 12345)

    # Bind the IP and port with the socket
    server_socket.bind(server_address)

    # Start listening for incoming requests
    server_socket.listen(1)
    print("Waiting for a connection...")

    try:
        while True:
            # Accept a connection when a client connects
            connection_socket, client_address = server_socket.accept()
            print("Connection established with:", client_address)

            while True:
                # Receive data from the client
                data = connection_socket.recv(1024).decode()

                if data.lower() == "stop":
                    print("Connection closed by the client.")
                    break

                print("Received from client:", data)

                # Send a response to the client
                connection_socket.sendall("Message received".encode())

            # Close the connection socket
            connection_socket.close()

    finally:
        # Close the listening socket
        server_socket.close()

if __name__ == "__main__":
    main()
