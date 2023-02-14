n = int(input())
a = [['.'] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i == j or (i + j) == (n - 1) or i == n//2 or j == n//2:
            a[i][j] = '*'
for row in a:
    for elem in row:
        print(elem,end=' ')
    print()