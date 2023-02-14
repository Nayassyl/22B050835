n , m = [int(s) for s in input().split()]
a = [['.'] * m for i in range(n)]
for i in range(n):
    for j in range(m):
        if ( i + j) % 2 == 1:
            a[i][j] = '*'
for row in a:
    for elem in row:
        print(elem, end = ' ')
    print()
