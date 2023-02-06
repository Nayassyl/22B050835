n = int(input())
a = 0
b = 1
i = 3
if n == 0:
    print (0)
elif n == 1 or n == 2:
    print(1)
else:
    while i <= n:
     c = a + b
     a = b
     b = c
     i += 1
    print(c + a)