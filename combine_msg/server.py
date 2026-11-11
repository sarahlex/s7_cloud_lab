import socket
import threading

clients =[]
msgs=[]
lock =threading.Lock()

def handle_client(c):
  while True:
    try:
      msg= c.recv(1024).decode()
      if not msg : 
        break
      with lock:
        msgs.append(msg)
        if len(msgs)==2:
          combined=" ".join(msgs)
          msgs.clear()
        else:
          combined=None
      if combined:
        for client in clients[:]:
          client.sendall(combined.encode())
    except:
      break
  with lock:
    if c in clients:
      clients.remove(c)
  c.close()
      
  
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',1234))
s.listen()
print("listening...")
while True:
  c,addr = s.accept()
  clients.append(c)
  threading.Thread(target=handle_client,args=(c,),daemon=True).start()
  
