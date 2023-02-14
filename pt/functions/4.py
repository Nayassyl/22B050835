def power(a, n):
    res = 1
    for i in range(abs(n)):
        res *= a
    return res

print(power(float(input()), int(input())))