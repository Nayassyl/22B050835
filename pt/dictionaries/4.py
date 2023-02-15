a = {}
for i in range(int(input())):
    words = [s for s in input().split()]
    for elem in words:
        a[elem] = a.get(elem, 0) + 1
max = 0
for x in a.values():
    if x > max:
        max = x
for elem in sorted(a):
    if max == a[elem]:
        print(elem)
        break

