n = int(input())
sum = 0
sum2 = 0
for x in range( 1, n + 1):
    sum += x
for i in range( n - 1):
    i = int(input())
    sum2 += i
print( sum - sum2 )