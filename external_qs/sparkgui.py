import tkinter as tk
from pyspark import SparkContext
from tkinter import filedialog,messagebox

sc= SparkContext('local','gui')


root=tk.Tk()
root.geometry("350x400")
root.title("spark")

chat = tk.Text(root,height =10,width=45)
chat.pack()
file_words=""

def  browser():
  global file_words
  filepath = filedialog.askopenfilename()
  text= sc.textFile(filepath)
  file_words = text.flatMap(lambda line: line.split())
  
browse  =tk.Button(root,text= 'browse',command = browser)
browse.pack()

def send():
  para = chat.get("1.0","end-1c")
  para_words = sc.parallelize(para.split())
  
  file_pairs = file_words.map(lambda word :(word,1))
  file_count = file_pairs.reduceByKey(lambda a,b :a+b)
  
  para_pairs = para_words.map(lambda word :(word,1))
  para_count = para_pairs.reduceByKey(lambda a,b :a+b)
  common  = file_count.join(para_count)
  
  output.delete("1.0","end")
  
  output.insert("end","Common words and their count :\n\n")
  for word,counts in common.collect():
    output.insert("end",f"{word}: File = {counts[0]}, Paragraph = {counts[1]}\n"
            )
  
  
compare = tk.Button(root,text = "compare",command=send)
compare.pack()

output = tk.Text(root,height=12,width = 45)
output.pack()

def close():
  sc.stop()
  root.destroy()

root.protocol("WM_DELETE_WINDOW", close)
root.mainloop()