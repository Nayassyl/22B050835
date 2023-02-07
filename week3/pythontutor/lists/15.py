n, k = [int(s) for s in input().split()]
listt = ['I'] * n
for m in range (k):
    l, r = [int(s) for s in input().split()]
    for j in range(l - 1, r):
        listt[j] = '.'
st = ''
for s in range(n):
    st += listt[s]
print(st)