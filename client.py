import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))
print("Connected to server. Type 'exit' to end chat.")
while True:
    # Send message
    msg = input("You: ")
    client_socket.send(msg.encode())

    if msg.lower() == "exit":
        print("You ended the chat.")
        break
    # Receive server reply
    reply = client_socket.recv(1024).decode()
    if reply.lower() == "exit":
        print("Server ended the chat.")
        break

    print(f"Server: {reply}")

client_socket.close()
