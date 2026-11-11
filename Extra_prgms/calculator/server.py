import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',1234))
s.listen()
print("waiting..")
c,addr = s.accept()
print("COnnected : ",addr)

while True:  
  data = c.recv(1024).decode()
  if not data: break
  msg = data.split()
  op1 =int(msg[0])
  op2 =int(msg[2])
  operator = msg[1]
  if  operator=="+":ans = op1+op2
  elif operator=="-":ans = op1-op2
  elif operator=="*":ans = op1*op2
  elif operator=="/":ans = op1/op2
  else: ans ="Invalid expression"
  c.sendall(f"Result = {ans}".encode())
c.close()
s.close()
  