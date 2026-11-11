from pyspark import SparkContext
sc= SparkContext('local','palindrome')
text = sc.textFile("palin.txt")
words =  text.flatMap(lambda line:line.split())
palin = words.filter(lambda word: word==word[::-1])
count = palin.count()
print("Palidnrome  :",palin.collect())
print("count = ",count)