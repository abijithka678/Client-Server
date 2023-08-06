import socket

def main():
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Server address and port
    server_address = ('localhost', 12345)

    # Connect to the server
    client_socket.connect(server_address)
    print("Connected to server.")

    try:
        while True:
            # Read data from standard input
            message = input("Enter a message: ")

            # Send data to the server
            client_socket.sendall(message.encode())

            if message.lower() == "stop":
                print("Connection closed.")
                break

            # Receive data from the server
            data = client_socket.recv(1024).decode()
            print("Received from server:", data)

    finally:
        # Close the socket
        client_socket.close()

if __name__ == "__main__":
    main()
