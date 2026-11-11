import socket

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(('localhost',5000))
server.listen(1)
print("Waiting for connection.....")
conn,add = server.accept()
print("Connected with :",add)
while True:
  msg = conn.recv(1024).decode()
  print("Client: ",msg)
  if not msg or msg=='bye':
    print("CONN CLOSED")
    break
  reply = input("Server:")
  conn.send(reply.encode())
  if not reply or reply=='bye':
      print("CONN CLOSED")
      break
conn.close()
server.close()
