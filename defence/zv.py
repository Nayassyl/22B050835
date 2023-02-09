n = int(input())
i = 1
while i <= n:
    print(('*' * ( i + i - 1)).center((2 * n) - 1, ' '))
    i += 1