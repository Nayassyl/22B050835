n = int(input())
i = n
while i >= 2:
    if n % i == 0:
        c = i
    i -=1
print(c)