n , k = [int(s) for s in input().split()]
s = set()
sum = 0
mm = []
for i in range(k):
    a_i, b_i = [int(s) for s in input().split()]
    j = 0
    while a_i + j * b_i <= n:
        m = a_i + j * b_i
        if m % 7 != 6 and m % 7 != 0:
             mm.append(m)
             s |= set(mm)
        j += 1
    mm = []
print(len(s))
