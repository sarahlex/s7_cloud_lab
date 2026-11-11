import socket
import threading

clients = []

def handle_client(c, addr):
    while True:
        try:
            msg, addr = c.recvfrom(1024)
            msg = msg.decode()

            if not msg:
                break

            for client in clients[:]:
                if client != addr:
                    c.sendto(msg.encode(), client)
        except:
            break

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 5000))

print("Server listening...")

while True:
    msg, addr = s.recvfrom(1024)

    if addr not in clients:
        clients.append(addr)
        print("NEW CONNECTION:", addr)

    for client in clients[:]:
        if client != addr:
            s.sendto(msg, client)