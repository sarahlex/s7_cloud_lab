import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',1234))
s.listen()

while True:
  c,addr = s.accept()
  while True:
    msg = c.recv(1024).decode()
    reverse = "Reversed = "+msg[::-1]
    c.sendall(reverse.encode())
  c.close()