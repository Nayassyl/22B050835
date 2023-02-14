n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j:
            a[i][j] = 0
        for k in range(1, n):
            if abs( i - j ) == k:
                a[i][j] = k
for row in a:
    for elem in row:
        print(elem,end=' ')
    print()