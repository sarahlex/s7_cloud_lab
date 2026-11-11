import socket
import threading
import tkinter as tk
from tkinter import simpledialog, messagebox

root = tk.Tk()
root.title("TCP Chat")
root.geometry("350x450") # Taller to fit the new text box

username = simpledialog.askstring("Username", "Enter your username:", parent=root)

if not username:
    root.destroy()
    exit()

try:
    c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c.connect(('127.0.0.1', 1234))
    # 1. Send username immediately upon connection
    c.sendall(username.encode())
except Exception as e:
    messagebox.showerror("Connection Error", str(e))
    root.destroy()
    exit()

chat = tk.Text(root, height=18, width=40)
chat.pack()

# 2. New entry box for the target user (Private messaging)
tk.Label(root, text="Send to (Leave blank to send to ALL):").pack()
target_entry = tk.Entry(root, width=30)
target_entry.pack()

tk.Label(root, text="Message:").pack()
entry = tk.Entry(root, width=30)
entry.pack()

def display(msg):
    chat.insert("end", msg + "\n")
    chat.see("end")

# 3. Modified Send message with private routing format
# Replaces your single send() function
def send_all():
    msg = entry.get().strip()
    if msg:
        display("You (To ALL): " + msg)
        c.sendall(f"ALL|{username}: {msg}".encode())
        entry.delete(0, "end")

def send_private():
    msg = entry.get().strip()
    target = target_entry.get().strip()
    if msg and target:
        display(f"You (Private to {target}): {msg}")
        c.sendall(f"{target}|[Private from {username}]: {msg}".encode())
        entry.delete(0, "end")

# Replaces your single SEND button
button_frame = tk.Frame(root)
button_frame.pack()
tk.Button(button_frame, text="SEND TO ALL", command=send_all).pack(side="left", padx=5)
tk.Button(button_frame, text="SEND PRIVATE", command=send_private).pack(side="left", padx=5)

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

# Start receiving thread
threading.Thread(target=receive, daemon=True).start()

# Handle window closing
root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()
