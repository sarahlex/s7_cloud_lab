import socket
import tkinter as tk
from tkinter import simpledialog,messagebox
import threading

root=tk.Tk()
root.geometry("350x400")
root.title("Claculator")

try:
  c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
  c.connect(('localhost',1234))
except Exception as e:
  messagebox.showerror("Error",str(e))
  root.destroy()
  exit()
  
chat =  tk.Text(root,height=18,width=40)
chat.pack()
entry = tk.Entry(root,width=30)
entry.pack()

def display(msg):
  chat.insert("end",msg+"\n")
  chat.see("end")
  
def send():
      msg= entry.get().strip()
      display("You: "+msg)
      c.sendall(msg.encode())
      entry.delete(0,"end")

def recieve():
  while True:
    try:
      msg = c.recv(1024).decode()
      root.after(0,display,msg)
    except:
      break
def close():
  c.close()
  root.destroy()

tk.Button(root,text="Calculate",command=send).pack()
threading.Thread(target = recieve,daemon=True).start()
root.protocol('WM_DELETE_WINDOW',close)
root.mainloop()