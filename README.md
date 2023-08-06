# Client-Server
Implementation of Client-Server Communication using Socket Programming TCP as transport layer Protocol
**Client-Server Communication using Socket Programming (TCP)**

This repository contains a basic implementation of client-server communication using socket programming in Python with TCP as the transport layer protocol. The client and server applications allow bidirectional communication between the client and server over a local network.

### Prerequisites
- Python 3.x

### How to Use
1. Clone the repository to your local machine.
2. Navigate to the `client_server_socket` directory.

#### Running the Server
1. Open a terminal or command prompt.
2. Run the server.py script using the following command:
   ```
   python server.py
   ```
3. The server will start listening for incoming connections.

#### Running the Client
1. Open another terminal or command prompt.
2. Run the client.py script using the following command:
   ```
   python client.py
   ```
3. The client will connect to the server, and you can start sending messages.

### Usage
1. After running the client application, you can enter messages in the terminal to send them to the server.
2. The server will display the received messages on its terminal.
3. The client will receive a simple acknowledgment message for each sent message.
4. To stop the communication and close the connection, enter "stop" (case insensitive) as a message in the client terminal.

### Important Notes
- The communication is designed to work on the local network for demonstration purposes.
- The server runs on the loopback address (localhost) and listens on port 12345 by default.
- The client connects to the server using the same address and port.
- The server can handle one client connection at a time. If another client wants to connect, it needs to wait until the current connection is closed.
- This is a basic implementation and may not handle all possible error cases.

### License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Acknowledgments
The implementation in this repository is inspired by various resources and tutorials on socket programming in Python. Special thanks to the Python community for providing valuable knowledge and examples.

Feel free to contribute to this project or use it as a reference for your own client-server communication applications! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request. Happy coding!
