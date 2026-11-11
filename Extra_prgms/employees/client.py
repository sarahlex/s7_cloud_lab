import socket
import threading
import tkinter as tk
from tkinter import simpledialog,messagebox

root = tk.Tk()
root.geometry("350x400")

username = simpledialog.askstring(
  "username",
  "enter name:",
  parent=root
)
if not username:
  root.destroy()
  exit()
root.title(f"{username} chat")
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',5000))

chat= tk.Text(root,height=18,width=40)
chat.pack()
entry = tk.Entry(root,width=30)
entry.pack()

def display(msg):
  chat.insert("end",msg+"\n")
  chat.see("end")
def send():
  msg = entry.get().strip()
  data = msg.split()[::-1]
  data = " ".join(data)
  try:
    c.sendall(f"{username}:{data}".encode())
    display("You: "+msg)
    entry.delete(0,"end")
  except:
    display("connection lost")

def receive():
  while True:
    try:
      msg =c.recv(1024).decode()
      if msg:
        root.after(0,display,msg)
    except:
      break
def close():
  c.close()
  root.destroy()
  
tk.Button(root,text="send",command=send).pack()
threading.Thread(target=receive,daemon=True).start()
root.protocol("WM_DELETE_WINDOW",close)
root.mainloop()