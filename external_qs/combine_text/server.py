import socket
import threading

clients=[]
msgs = []
lock=threading.Lock()
def handle_cleint(c):
  while True:
    try:
      text = c.recv(1024).decode()
      if not text: break
      with lock:
        msgs.append(text)
        if len(msgs)==2:
          combined = " ".join(msgs)
          msgs.clear()
        else: 
          combined=None
      if combined:
        for client in clients[:]:
          client.sendall(f"\nCOMBINED: {combined}".encode())
    except:
      break
  with lock:
    if c in clients:
      clients.remove(c)
  c.close()

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',1234))
s.listen()
while True:
  c,addr = s.accept()
  clients.append(c)
  threading.Thread(
    target = handle_cleint,
    args=(c,),
    daemon=True
  ).start()