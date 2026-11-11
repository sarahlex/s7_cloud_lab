import socket

s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind(('localhost',5000))

while True:
  msg,addr = s.recvfrom(1024)
  msg = msg.decode()
  x,num = msg.split()
  ans=""
  match x:
    case "even":
      if int(num)%2==0: ans ="True"
      else: ans ="False"
    case "odd":
      if int(num)%2!=0: ans="True"
      else: ans ="False"
    case "square": ans =str(int(num)*int(num))
    case "close": ans ="goodbye"
    case _: ans = "invalid input"
  s.sendto(ans.encode(),addr)
  if ans=="goodbye":
    break
s.close()    