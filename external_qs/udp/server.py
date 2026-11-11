import socket
from datetime import datetime
now =datetime.now()
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',1234))

while True:
  c,addr= s.recvfrom(1024)
  msg= c.decode()
  reply=""
  match msg:
    case "HELLO": reply= "Hello, client!"
    case "TIME": reply =str(now.time())
    case "DATE": reply= str(now.date())
    case "CLOSE": reply="Goodbye" 
    case _: reply="Invalid command. Please send a valid command."
  s.sendto(reply.encode(),addr) # MISTAKKEE SEND TO SERVER
  if reply=="Goodbye":
      break

s.close()
