import socket

qs = ["What is the capital of India?","Which language is used for AI?",
      "What is 5 + 5?","Which planet is known as the Red Planet?","What is the full form of CPU?"]
answer = ["Delhi","Python","10","Mars","Central Processing Unit"]
score=0

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(('localhost',1234))
s.listen()
print("server waiting..")
c, addr = s.accept()

for i in range(5):
  print(f"Question :{qs[i]}")
  try:
    c.sendall(f"server: Question {i+1}-{qs[i]}".encode())
    ans = c.recv(1024).decode()
    if not ans : break
    if ans==answer[i]: score+=10
    print("Answer: ",ans)
  except:
    break
c.sendall(f"Score = {score}".encode())
print("FInal score: ",score)
c.close()
s.close()