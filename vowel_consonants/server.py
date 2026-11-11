import socket

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('127.0.0.1',5000))
s.listen(1)

while True:
  c,addr = s.accept()
  str = c.recv(1024).decode()
  vowels =0
  consonants=0
  
  for ch in str:
    if ch.lower() in 'aeiou':
      vowels+=1
    elif ch.isalpha():
      consonants+=1
  
  c.sendall(f"Vowels = {vowels}\n Consonants = {consonants}".encode())
  c.close()