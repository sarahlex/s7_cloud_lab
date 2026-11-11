import socket
import threading
import tkinter as tk
from tkinter import simpledialog,messagebox

root = tk.Tk()
root.geometry("350x400")
root.title("Calculator")

c= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',1234))

chat=  tk.Text(root,height=18,width=40)
chat.pack()
entry = tk.Entry(root,width=30)
entry.pack()

def display(msg):
  chat.insert("end",msg+"\n")
  chat.see("end")
def send():
  msg = entry.get().strip()
  try:
    display("you: "+msg)
    c.sendall(msg.encode())
    entry.delete(0,"end")
  except:
    display('bad connection')
def receive():
  while True:
    try:
      msg = c.recv(1024).decode()
      if not msg : break
      root.after(0,display,msg)
    except:
      break
def close():
  c.close()
  root.destroy()

tk.Button(root,text="calculate",command=send).pack()
threading.Thread(target = receive,daemon=True).start()
root.protocol("WM_DELETE_WINDOW",close)
root.mainloop()

      