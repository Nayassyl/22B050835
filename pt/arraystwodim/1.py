n , m = [int(s) for s in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]
max = a[0][0]
x , y = 0, 0
for i in range(n):
    for j in range(m):
        if a[i][j] > max:
            max = a[i][j]
            x, y = i, j
print(x , y)