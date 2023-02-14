n, m = [int(s) for s in input().split()]
s = set()
l = set()
for i in range(n):
    s.add(int(input()))
for i in range(m):
    l.add(int(input()))

print(len(s.intersection(l)))
print(*[str(i) for i in sorted(s.intersection(l))])
print(len(s.difference(l)))
print(*[str(i) for i in sorted(s.difference(l))])
print(len(l.difference(s)))
print(*[str(i) for i in sorted(l.difference(s))])


