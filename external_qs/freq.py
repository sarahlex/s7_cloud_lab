from pyspark import SparkContext
sc= SparkContext('local','freq')
text  =sc.textFile("palin.txt")

words = text.flatMap(lambda line: line.split())
pairs = words.map(lambda word: (word,1))
count = pairs.reduceByKey(lambda a,b : a+b)
sorted_words = count.sortBy(lambda x: x[1],ascending=False)
print("top 5 words are:")
for pair in sorted_words.collect()[:5]:
  print(pair)
sc.stop()