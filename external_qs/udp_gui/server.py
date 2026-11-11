import socket

# We store addresses (IP, port) instead of socket objects
clients = set()

# Start UDP server (SOCK_DGRAM)
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1', 1234))

print("UDP Server waiting...")

# No threading needed! One loop handles all incoming packets.
while True:
    try:
        # recvfrom gives us the message AND the sender's address
        msg, addr = s.recvfrom(1024)
        
        # If this is a new address, add it to our known clients
        if addr not in clients:
            clients.add(addr)
            print("New client:", addr)
            
        # Broadcast the message to everyone EXCEPT the sender
        for client in clients:
            if client != addr:
                s.sendto(msg, client)
    except:
        pass