import socket

c=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server_addr = ('localhost',1234)

while True:
  command = input("You: ")
  c.sendto(command.encode(),server_addr)
  data,_ = c.recvfrom(1024)
  reply = data.decode()
  
  print(f"server: {reply}")
  if reply=="Goodbye":
      break
c.close()