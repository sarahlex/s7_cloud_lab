import socket 
client =  socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_add = ('localhost',5001)
while True:
  reply = input("CLinet; ")
  client.sendto(reply.encode(),server_add)
  data,_ = client.recvfrom(1024)
  print("Server: ",data.decode())
client.close()