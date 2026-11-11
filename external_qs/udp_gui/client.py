import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.title("UDP Chat")
root.geometry("350x400")

username = simpledialog.askstring("Username", "Enter your username:", parent=root)
if not username:
    root.destroy()
    exit()

# UDP Socket
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SERVER_ADDR = ('127.0.0.1', 1234) # Define server address here

chat = tk.Text(root, height=18, width=40)
chat.pack()

entry = tk.Entry(root, width=30)
entry.pack()

def display(msg):
    chat.insert("end", msg + "\n")
    chat.see("end")

def send():
    msg = entry.get().strip()
    if msg:
        try:
            # Use sendto() instead of sendall()
            c.sendto(f"{username}:{msg}".encode(), SERVER_ADDR)
            display("You: " + msg)
            entry.delete(0, "end")
        except:
            display("Error sending message.")

def receive():
    while True:
        try:
            # Use recvfrom() instead of recv()
            msg, _ = c.recvfrom(1024)
            root.after(0, display, msg.decode())
        except:
            break

def close():
    c.close()
    root.destroy()

tk.Button(root, text="SEND", command=send).pack()

# Start receiving thread (still needed on client to not freeze the GUI)
threading.Thread(target=receive, daemon=True).start()

# Join notification
c.sendto(f"{username} has joined the chat.".encode(), SERVER_ADDR)

root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()