def downn(n):
    for i in range(n, 0, -1):
        yield i
for x in downn(int(input())):
    print(x, end = " ")