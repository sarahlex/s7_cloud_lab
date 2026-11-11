from pyspark import SparkContext

sc = SparkContext('local','wordCount')
text = sc.textFile('wordcount.txt')
words = text.flatMap(lambda line: line.split())
pair = words.map(lambda word: (word,1))
counts = pair.reduceByKey(lambda a,b: a+b)

for pair in counts.collect():
  print(pair)
  
sc.stop()