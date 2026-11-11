from pyspark import SparkContext 

sc = SparkContext('local','common')
text1 = sc.textFile('f1.txt')
text2 = sc.textFile('f2.txt')

w1 = text1.flatMap(lambda line: line.split())
w2 = text2.flatMap(lambda line: line.split())

result  = w1.intersection(w2)

print(result.collect())
sc.stop()

