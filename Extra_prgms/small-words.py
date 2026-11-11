from pyspark import SparkContext
sc= SparkContext('local','smaller_words')

text = sc.textFile("text.txt")
words = text.flatMap(lambda line: line.split())
three = words.filter(lambda word: len(word)<3)
print("words less than 3 letters:",three.collect())
rest = words.filter(lambda word: len(word)>2)
pairs = rest.map(lambda word: (word,1))
reuslt  = pairs.reduceByKey(lambda a,b : a+b)
for pair in reuslt.collect():
  print(f"{pair[0]} : {pair[1]}")

