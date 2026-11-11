from pyspark import SparkContext

sc= SparkContext('local','longest')

text = sc.textFile('wordcount.txt')
words = text.flatMap(lambda line:line.split())
longest = words.reduce(lambda a,b: a if len(a)> len(b) else b)

print("The longest word is: ",longest)
sc.stop()