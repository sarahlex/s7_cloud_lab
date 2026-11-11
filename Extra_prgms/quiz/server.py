import socket

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',1234))
s.listen()
print('server listening...')
qs = ["What is the capital of India?","Which language is used for AI?",
      "What is 5 + 5?","Which planet is known as the Red Planet?","What is the full form of CPU?"]
answer = ["Delhi","Python","10","Mars","Central Processing Unit"]


while True:
  c,addr = s.accept()
  score=0
  print("Connected :",addr)
  for i in range(5):
    c.sendall(f"Server: Question {i+1}: {qs[i]}".encode())
    print(f"Question {i+1}: {qs[i]}")
    
    ans = c.recv(1024).decode()
    if not ans:
      break
    print(f"Answer: {ans}")
    
    if ans==answer[i]:
      score+=10
  c.sendall(f"Final Score: {score}/50".encode())
  print(f"Final Score: {score}/50")
  c.close()
  
