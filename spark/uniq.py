from pyspark import SparkContext

sc = SparkContext('local','uniq')
text = sc.textFile('wordcount.txt')
words = text.flatMap(lambda line: line.split())
result = words.distinct()
print("Distinct words are:")
for word in result.collect():
  print(word)
sc.stop()