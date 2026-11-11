import socket
import threading

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',1234))
s.listen()
print("waitng..")
clients=[]

def handle(c):
  while True:
    try:
      msg = c.recv(1024)
      if not msg: 
        break
      for x in clients[:]:
        if x!=c:
          x.sendall(msg)
    except:
      print("error")
      break
  if c in clients: clients.remove(c)
  c.close()

while True:
  c,add = s.accept()
  print('connected with:',add)
  clients.append(c)
  threading.Thread(target=handle,args=(c,),daemon=True).start()
  