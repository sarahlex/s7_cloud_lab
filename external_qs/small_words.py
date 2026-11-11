from pyspark import SparkContext
sc= SparkContext('local','small')

text = sc.textFile("uniq.txt")
words = text.flatMap(lambda line: line.split())
small = words.filter(lambda word: len(word)<3)
rest =  words.filter(lambda word: len(word)>=3)
count = rest.count()
print("Small words: ",small.collect())
print("others: ",rest.collect())
print("count: ",count)
