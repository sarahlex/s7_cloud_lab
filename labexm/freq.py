from pyspark import SparkContext

sc= SparkContext('local','freq')
text = sc.textFile("text.txt")
words = text.flatMap(lambda line: line.split())
pairs = words.map(lambda word: (word.lower(),1))
count = pairs.reduceByKey(lambda a,b :a+b)
freq = count.sortBy(lambda x: x[1],ascending=True)
print('top least 5 freq')
for pair in freq.collect()[:5]:
  print(pair)
sc.close()