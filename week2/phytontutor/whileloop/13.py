x = -1
max = 0 
i = 0
while x!= 0:
    x = int(input())
    if x > max:
        max = x
        i = 1
    elif x == max:
        i += 1
print( i )