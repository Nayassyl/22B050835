l = 8
x = []
y = []
for i in range(l):
    n, k = [int(s) for s in input().split()]
    x.append(n)
    y.append(k)
c = True
for i in range(8):
    for j in range( i + 1 , l):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            c = False
if c : 
    print("NO")
else: 
    print("YES")