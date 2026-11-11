from pyspark import SparkContext

sc= SparkContext("local","palindrome")

text = sc.textFile("text.txt")
words = text.flatMap(lambda line: line.split())
palindrom = words.filter(lambda word: word==word[::-1])
count = palindrom.count()
print("No. of palindrome words:",count)
print("Words are: ",palindrom.collect())