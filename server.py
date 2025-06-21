import socket

HOST = ''  # same as '0.0.0.0'
# Empty means that the server will listen on all available interfaces of the machine (both localhost and network IP).
# This allows the server to accept connections from any IP address that can reach it.   
# If you want to restrict it to a specific IP address, you can set it to '


LISTENING_PORT = 5000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # An IPv4 socket (AF_INET) of type TCP (SOCK_STREAM) is created.
    # The use of with ensures that the socket is automatically closed at the end of the block.

    s.bind((HOST, LISTENING_PORT)) # The socket is bound to the specified host and port.
    s.listen()                     # The socket is set to listen for incoming connections.
    print(f"Waiting for connection at port {LISTENING_PORT}...")

    conn, addr = s.accept() # Accepts a connection from a client.
                            # Waits until a client connects.
                            # Socket is blocking until client connection.
                            # accept() blocks and waits for a client to connect.
                                # conn: new socket dedicated to communication with the client.
                                # addr: IP address and port of the client.

    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024) # Receives data from the client.
                                   # bufsize reads up to 1024 bytes from the client.
                                   # This is a blocking call, meaning it waits until data is received.

            if not data: # If no data is received, the connection is closed.
                break
            print(f"Received: {data.decode()}") # Message is decoded.
            conn.sendall(b"Message received")  # Sends a response back to the client.
