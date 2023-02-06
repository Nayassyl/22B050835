x = int(input())
max = 0
i = 0

while x != 0:
    i += 1
    if x > max:
        max = x
        c = i
    x = int(input())
print(c - 1)