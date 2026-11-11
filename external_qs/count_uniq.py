from pyspark import SparkContext

sc= SparkContext('local','uniq')

text = sc.textFile("uniq.txt")
words = text.flatMap(lambda line: line.split())
uniq = words.distinct()
count = uniq.count()
print("No. of uniq words: ",count)
print('the words are: ',uniq.collect())