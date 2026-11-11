
import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.title("TCP Chat")
root.geometry("350x400")

username = simpledialog.askstring("Username", "Enter your username:", parent=root)

if not username:
    root.destroy()
    exit()

try:
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(('127.0.0.1',1234))
except Exception as e:
    messagebox.showerror("Connection Error", str(e))
    root.destroy()
    exit()

chat = tk.Text(root, height=18, width=40)
chat.pack()

entry = tk.Entry(root, width=30)
entry.pack()

def display(msg):
    chat.insert("end", msg + "\n")
    chat.see("end")

# Send message
def send():
    msg = entry.get().strip()
    if msg:
        try:
            c.sendall(f"{username}:{msg}".encode())
            display("You: " + msg)
            entry.delete(0, "end")
        except:
            display("Connection lost.")

def receive():
    while True:
        try:
            msg = c.recv(1024).decode()
            if not msg:
                break
            root.after(0, display, msg)
        except:
            break
# Close chat window
def close():
    c.close()
    root.destroy()

# Send button
tk.Button(root, text="SEND", command=send).pack()

# Start receiving thread
threading.Thread(target=receive, daemon=True).start()

# Join notification
c.sendall(f"{username} has joined the chat.".encode())

# Handle window closing
root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
