n = int(input())
sum = 0
fac = 1
for x in range( 1, n + 1):
    fac *= x
    sum += fac
print(sum)