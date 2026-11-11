import socket

c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('127.0.0.1',5000))

str = input("Enter a string: ")
c.sendall(str.encode())
reuslt =""

while True:
  msg = c.recv(1024).decode()
  if not msg: break
  reuslt+=msg
  
print(reuslt)
c.close()