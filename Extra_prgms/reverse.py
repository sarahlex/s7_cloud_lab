from pyspark import SparkContext
sc= SparkContext('local','reverse')

text = sc.textFile("text.txt")
words = text.flatMap(lambda line: line.split())
reversed = words.map(lambda word: word[::-1])
print("Reversed text ="," ".join(reversed.collect()))

chars = text.flatMap(lambda line: list(line) ).map(lambda ch : not ch.isspace()).count()
print("Count of characters= ",chars)
