n = int(input())
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(n):
        if i + j == n - 1:
            a[i][j] = 1
        elif i + j >= n:
            a[i][j] = 2
for row in a:
    for elem in row:
        print(elem,end=' ')
    print()