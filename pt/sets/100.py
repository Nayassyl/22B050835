n , k = [int(s) for s in input().split()]
s = set([str(s) for s in range(n + 1)])
mm = set()
for i in range(k):
    a_i, b_i = [int(s) for s in input().split()]
    j = 0
    while a_i + j * b_i <= n:
        m = a_i + j * b_i
        mm.update(str(m))
        s.remove(m)
        j += 1
print(len(s))