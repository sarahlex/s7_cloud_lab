import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',5000))
s.listen(1)
print("Waiting....")
while True:  #REST EVERYTHING INSIDE WHILE LOOP
  c,addr = s.accept()
  words = c.recv(1024).decode()
  old,new=  words.split()

  with open("text.txt","r") as f:
    content = f.read()
    
  content = content.replace(old,new) #STORE THE REPLACED CONTENT
  
  with open("text.txt","w") as f:
    f.write(content)

  c.sendall(content.encode())
  c.close()
