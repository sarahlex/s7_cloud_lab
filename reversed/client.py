import socket
import tkinter as tk
import threading
from tkinter import messagebox, simpledialog

root = tk.Tk()
root.geometry("350x400")
username = simpledialog.askstring("Username","ENter username:",parent =root)

if not username:
  root.destroy()
  exit()
  
root.title(username+" chat")
try:
  c = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  c.connect(('localhost',1234))
except Exception as e:
  messagebox.showerror("Error",str(e))
  root.destroy()
  exit()
chat = tk.Text(root,height=18,width=40)
chat.pack()

entry = tk.Entry(root,width=30)
entry.pack()
def display(msg):
  chat.insert("end",msg+"\n")
  chat.see("end")
  
def send():
  msg = entry.get().strip()
  if msg:
    display(username+": "+msg)
    c.sendall(msg.encode())
    entry.delete(0,"end")
def receive():
  while True:
    try:
      msg = c.recv(1024).decode()
      if not msg:
        break
      root.after(0,display,msg)
    except:
      break
    
      
def close():
  c.close()
  root.destroy()
  
tk.Button(root,text="CLICKKKK", command=send).pack()

threading.Thread(target = receive,daemon=True).start()
  
root.protocol("WM_DELETE_WINDOW",close)
root.mainloop()
  