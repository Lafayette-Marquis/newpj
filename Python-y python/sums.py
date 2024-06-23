import math

def sumTo(n):
  sum = 0
  for i in range(1, n+1):
    sum += i
  return sum

sumTos = input("Enter a number: ")
print(sumTo(int(sumTos)))