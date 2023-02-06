x = int(input())
a = x
i = 0
while x!= 0:
    x = int(input())
    if x > a:
        i += 1
    a = x
print(i)