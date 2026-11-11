import socket
import threading

# Use a dictionary to map {username: socket}
clients = {}

def handle_client(c, addr):
    print("Connected with:", addr)
    try:
        # 1. Safely receive just the username first
        username = c.recv(1024).decode()
        clients[username] = c
        
        # 2. Server handles the join broadcast (prevents packet merging)
        join_msg = f"{username} has joined the chat."
        for user, client_sock in clients.items():
            if client_sock != c:
                client_sock.sendall(join_msg.encode())
        
        while True:
            msg = c.recv(1024).decode()
            if not msg:
                break
            
            # Route the message based on "TARGET|MESSAGE" format
            if "|" in msg:
                target, actual_msg = msg.split("|", 1)
                
                if target == "ALL":
                    for user, client_sock in clients.items():
                        if client_sock != c:
                            client_sock.sendall(actual_msg.encode())
                elif target in clients:
                    clients[target].sendall(actual_msg.encode())
    except:
        pass
        
    if username in clients:
        del clients[username]
        # Optional: broadcast when someone leaves
        leave_msg = f"{username} has left the chat."
        for user, client_sock in clients.items():
            client_sock.sendall(leave_msg.encode())
            
    c.close()
    print("Disconnected:", addr)

# Start server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 1234))
s.listen()

print("Server waiting...")

while True:
    c, addr = s.accept()
    threading.Thread(
        target=handle_client,
        args=(c, addr),
        daemon=True
    ).start()