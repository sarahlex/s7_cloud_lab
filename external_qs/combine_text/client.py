import socket
import threading
import tkinter as tk

root= tk.Tk()
root.geometry("350x400")
root.title("chat")

c= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',1234))

chat=  tk.Text(root,height =18, width=45)
chat.pack()

def display(msg):
  output.insert("end",msg+"\n")
  output.see("end")
  
def send():
  text = chat.get("1.0","end-1c")
  try:
    c.sendall(text.encode())
    chat.delete("1.0","end")
  except:
    display("connection lost")
def receive():
  while True:
    try:
      msg = c.recv(1024).decode()
      if not msg: break
      output.delete("1.0","end")
      root.after(0,display,msg)
    except:
      break
def close():
  c.close()
  root.destroy()
output = tk.Text(root,height=12,width=45)
output.pack()

tk.Button(root,text ="combine",command=send).pack()
threading.Thread(target=receive,daemon=True).start()
root.protocol("WM_DELETE_WINDOW",close)
root.mainloop()
