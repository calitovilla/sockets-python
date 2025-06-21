import socket

HOST = '192.168.0.13'  # Server IP address
PORT = 5000 # Listening port of the server


# Create a socket and connect to the server
## The socket is created with the same parameters as the server: IPv4 and TCP.

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #s.bind(('0.0.0.0', 12345)) # Bind to all interfaces on port 12345 
                                # This is optional, as the client does not need to bind to a specific port.
                                # '' or '0.0.0.0' means that the client can accept connections from any IP address.

    s.connect((HOST, PORT)) # Connect to the server at the specified IP address and port
    s.sendall(b"Hello from the PC!") # Send a message to the server
    data = s.recv(1024) # Receive a response from the server 
                        # waits until the server sends a response.
                        # The buffer size is set to 1024 bytes, meaning it can receive up to 1024 bytes of data.

print(f"Server response: {data.decode()}")
