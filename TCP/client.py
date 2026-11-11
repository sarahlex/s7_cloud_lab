import socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(("localhost",5000))
while True:
  msg = input("Client: ")
  client.send(msg.encode())
  if not msg or msg=='bye':
      print("CONN CLOSED")
      break
  reply= client.recv(1024).decode()
  
  print("Server: ",reply)
  if not reply or reply=='bye':
      print("CONN CLOSED")
      break
client.close()
