import socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('127.0.0.1', 12345))
server_socket.listen(1)
print("Server is waiting for connection...")
conn, addr = server_socket.accept()
print(f"Connected with {addr}")

while True:
    # Receive message from client
    client_msg = conn.recv(1024).decode()
    if client_msg.lower() == "exit":
        print("Client ended the chat.")
        break
    print(f"Client: {client_msg}")

    # Send reply to client
    server_msg = input("Server: ")
    conn.send(server_msg.encode())

    if server_msg.lower() == "exit":
        print("Server ended the chat.")
        break

conn.close()
server_socket.close()
# Hello i am shagor