import socket

# Create a socket object
# AF_INET: Address Family - Internet
# AF_INET6: Address Family - Internet version 6
# SOCK_STREAM: Socket Type - Stream
# SOCK_DGRAM: Socket Type - Datagram

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    client_socket.connect(("192.168.0.196", 8080))

    # Send data to the server
    client_socket.sendall(b"Hello from the client!")

    # Receive data from the server
    data = client_socket.recv(1024)
    print("Received:", data.decode())
finally:
    # Close the client socket
    client_socket.close()
