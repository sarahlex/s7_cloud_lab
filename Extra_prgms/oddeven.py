from pyspark import SparkContext

sc=SparkContext('local','oddeven')
text = sc.textFile("numbers.txt")
words = text.flatMap(lambda line:line.split())
nums = words.map(lambda num: int(num))
even,odd=0,0
for num in nums.collect():
  if num %2==0:
    even+=num
  else:
    odd+=num
print("SUm of odd no.s = ",odd)
print("sum of even no. = ",even)