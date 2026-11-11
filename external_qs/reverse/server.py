import socket
import threading

clients =[]
def handle_client(c):
  while True:
    try:
      msg= c.recv(1024).decode()
      if not msg: break
      for client in clients[:]:
        if client!=c:
          client.sendall(msg.encode())
    except:
      break
  if c in clients:
    clients.remove(c)
  c.close()
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',5000))
s.listen()
print("lsitening")
while True:
  c,addr = s.accept()
  clients.append(c)
  threading.Thread(target=handle_client,
                   args = (c,),
                   daemon=True).start()
  