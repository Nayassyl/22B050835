n, m = [int(s) for s in input().split()]
a = [[0] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if i == j:
            a[i][j] = 1
        elif j < i:
            a[i][j] = 2

for row in a:
    for elem in row:
        print(elem, end = " ")
    print()