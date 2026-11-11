import socket
import threading
import tkinter as tk

c=  socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',1234))

root = tk.Tk()
root.title("chatt")
root.geometry("300x350")

chat = tk.Text(root,width=35,height=15)
chat.pack()

entry = tk.Entry(root,width=25)
entry.pack()

def send():
  msg = entry.get().strip()
  c.sendall(msg.encode())
  chat.insert("end","you:"+msg+"\n")
  entry.delete(0,"end")
  
def recive():
  while True:
    try:
      msg = c.recv(1024).decode()
      if not msg:
        break
      chat.insert("end","Other: "+msg+"\n")
    except:
      print("error")
      break
    

tk.Button(root,text='Send',command=send).pack()
threading.Thread(target=recive,daemon=True).start()
root.mainloop()