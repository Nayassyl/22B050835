a = {}
for i in range(int(input())):
    words = [s for s in input().split()]
    for elem in words:
        a[elem] = a.get(elem, 0) + 1
b = {}
for elem in sorted(a):
    b[a[elem]] = b.get(a[elem], "") + elem + " "

for elem in sorted((b), reverse = True):
    print(b[elem], end = " ")
