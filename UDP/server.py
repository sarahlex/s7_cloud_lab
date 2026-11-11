import socket

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(('localhost',5001))

while True:
  data,addr =  server.recvfrom(1024)
  msg= data.decode()
  print("CLient: ",msg)
  if not msg or msg=='bye':
    print("CONN CLOSED")
    break
  reply = input("server: ")
  server.sendto(reply.encode(),addr)
server.close()