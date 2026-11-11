from pyspark import SparkContext

sc = SparkContext('local','fivechar')
text = sc.textFile('wordcount.txt')
words = text.flatMap(lambda line: line.split())
result = words.filter(lambda word: len(word)>5)
print('The words are:')
for word in result.collect():
  print(word)
  
sc.stop()