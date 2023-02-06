from math import sqrt
x = int(input())
n = 0
sum = 0
sumst = 0
while x != 0:
    n += 1
    sum += x
    sumst += x ** 2
    x = int(input())
print(sqrt( (sumst - sum ** 2 / n) / ( n - 1 ) ))
    