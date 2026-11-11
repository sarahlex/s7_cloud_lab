import socket

c =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
c.connect(('localhost',5000))

old = input("Enter word to be replaced")
new =input("Enter replcamenet word:")

c.sendall(f"{old} {new}".encode())
reuslt =""

while True:   #LEARN THIS ,DONT FORGET WHILEEE
  data = c.recv(1024).decode()
  if not data:break
  reuslt+=data #APPEND RESULT
print("Content\n",reuslt)
c.close()