import socket
import threading
c= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',1234))

num = input("You: ")
c.sendall(num.encode())
result = c.recv(1024).decode()
print("Reuslt: ")
print(result)

c.close()
