n = int(input())
a = {}
for i in range(n):
    x, y = [ s for s in input().split()]
    a[x] = y
s = input()
for x in a:
    if a[x] == s:
        print(x)
    elif x == s:
        print(a[x])