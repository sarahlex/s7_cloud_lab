import socket
import threading

clients = []

def handle_client(c, addr):
    print("Connected with:", addr)
    while True:
        try:
            msg = c.recv(1024)
            if not msg:
                break
            for client in clients[:]:
                if client!=c:
                    client.sendall(msg)                  
        except:
            break
    if c in clients:
        clients.remove(c)
    c.close()
    print("Disconnected:", addr)

# Start server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1',1234))
s.listen()

print("Server waiting...")

while True:
    c, addr = s.accept()
    clients.append(c)
    threading.Thread(
        target=handle_client,
        args=(c, addr),
        daemon=True
    ).start()
