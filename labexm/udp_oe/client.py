import socket

c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_addr = ('localhost',5000)

while True:
  msg = input('You: ')
  c.sendto(msg.encode(),server_addr)
  data,_ = c.recvfrom(1024)
  reply= data.decode()
  print("server: ",reply)
  if reply=='goodbye':
    break
c.close()