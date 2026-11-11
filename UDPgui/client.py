import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.geometry("350x400")

username = simpledialog.askstring("Username", "Enter username:", parent=root)

if not username:
    root.destroy()
    exit()

root.title(username + " chat")

c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_addr = ('localhost', 5000)

chat = tk.Text(root, width=40, height=18)
chat.pack()

entry = tk.Entry(root, width=30)
entry.pack()

def display(msg):
    chat.insert("end", msg + "\n")
    chat.see("end")

def send():
    msg = entry.get().strip()

    if msg:
        c.sendto(f"{username}: {msg}".encode(), server_addr)
        display("You: " + msg)
        entry.delete(0, "end")

def receive():
    while True:
        try:
            data, addr = c.recvfrom(1024)
            msg = data.decode()
            root.after(0, display, msg)
        except:
            break

def close():
    c.close()
    root.destroy()

tk.Button(root, text="Send", command=send).pack()

threading.Thread(target=receive, daemon=True).start()

c.sendto(f"{username} has joined.".encode(), server_addr)

root.protocol("WM_DELETE_WINDOW", close)

root.mainloop()