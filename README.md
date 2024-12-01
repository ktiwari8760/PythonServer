# PythonServer

WebSockets are used for persistent communication between a client
and a server , While in HTTP the connection is not made a request/response model is followed.

Initiated from the client end a handshake is made between the client and the server here server can make the connection 
as follows : 

s.connect((HOST, PORT))  # Connect to the server

s.sendall(b"Hello, world") # This sends the message to the server

data = conn.recv(1024)  # Receive data from the client

Unless and until the connection is closed the communication channel remains open.

Advantages of it are as follows :

1 ) Bidirectional ( server  & client both can send and receive the message)
2 ) Low Latency
3 ) Lightweight
4 ) Website maintains a persistent connection , which reduces latency compared to stateless HTTP.

