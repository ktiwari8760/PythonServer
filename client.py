import socket

HOST = "IP OF SERVER / Local Host"
PORT = 9090

# Using a context manager to automatically close the socket when done
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))  # Connect to the server
    s.sendall(b"Hello, world")
    s.sendall(b"HOW ARE YOU BRO")# Send a message to the server
    data = s.recv(1024)  # Receive data back from the server

print(f"Received: {data.decode()}")  # Decode and print the received data
