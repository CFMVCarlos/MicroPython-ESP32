import socket

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a host and port
server_socket.bind(("0.0.0.0", 8080))

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening...")

# Accept a connection
client_socket, addr = server_socket.accept()
print("Connected to:", addr)

try:
    # Receive data from the client
    data = client_socket.recv(1024)
    print("Received:", data.decode())

    # Send a response back to the client
    client_socket.sendall(b"Hello from the server!")
finally:
    # Close the client socket
    client_socket.close()

# Close the server socket
server_socket.close()
