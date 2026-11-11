import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',1234))
s.listen()
print("listening...")
c,addr=s.accept()

while True:
  msg = c.recv(1024).decode().split()
  if not msg:
    break
  op1= int(msg[0])
  opr = msg[1]
  op2 =int(msg[2])
  ans=0
  match opr:
    case "+": ans =op1+op2
    case "-":ans=op1-op2
    case "*":ans=op1*op2
    case "/": ans=op1/op2
    case _: ans ="Invalid Operator"
  c.sendall(f"Result = {ans}".encode())
c.close()
s.close() 
  
  