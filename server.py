import socket

# Setup listening socket
HOST = "Ip of Network / LocalHost"
PORT = 9090

# Using a context manager to automatically close the socket when done
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))  # Bind to the given host and port
    s.listen()  # Start listening for incoming connections
    print(f"Server listening on {HOST}:{PORT}")

    conn, addr = s.accept()  # Accept an incoming connection
    with conn:
        print(f"The connection is made with the client: {addr}")

        # Communicate with the client
        while True:
            data = conn.recv(1024)  # Receive data from the client
            if not data:
                break  # Exit if no data is received (client disconnected)
            conn.sendall(data)  # Echo the received data back to the client
