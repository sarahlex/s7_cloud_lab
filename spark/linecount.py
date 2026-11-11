from pyspark import SparkContext

sc=  SparkContext('local','linecount')

text = sc.textFile('wordcount.txt')
count = text.count()
print('No. fo lines =',count)

sc.stop()