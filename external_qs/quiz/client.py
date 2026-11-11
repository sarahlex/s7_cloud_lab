import socket

c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',1234))

for i in range(5):
  qs = c.recv(1024).decode()
  print(qs)
  ans = input("you: ")
  c.sendall(ans.encode())
score= c.recv(1024).decode()
print(score)
c.close()