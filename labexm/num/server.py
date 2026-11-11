import socket
import threading
clients=[]
msgs =[]
lock = threading.Lock()
def handle(c):
  while True:
    try:
      msg = c.recv(1024).decode()
      if not msg :break
      with lock:
        msgs.append(msg)
        if len(msgs)==2:
          combined = " ".join(msgs)
          msgs.clear()
        else:
          combined=None
      if combined:
        nums = [int(num) for num in combined.split()]
        dist_num = list(set(nums))
        dist_num.sort()
        total = sum(dist_num)
        average = total/len(dist_num)
        result = f"SORTED NUM: {dist_num}\n"
        result += f"sum = {total}\n"
        result += f"avg = {average}"

        for client in clients[:]:
            client.sendall(result.encode())
    except:
      break
  with lock:
    if c in clients:
      clients.remove(c)
  c.close()

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',1234))
s.listen()
while True:
  c,addr = s.accept()
  clients.append(c)
  threading.Thread(target = handle,args=(c,),daemon= True).start()
