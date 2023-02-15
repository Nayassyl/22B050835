n = int(input())
a = {}
for i in range(n):
    x, y = input().split()
    a[x] = a.get(x, 0) + int(y)
for elem in sorted(a):
    print(elem, a[elem])