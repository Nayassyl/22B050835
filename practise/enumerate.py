a = [int(s) for s in input().split()]
for i, num in enumerate(a):
    if num % 2 == 0:
        print(i, end = " ")