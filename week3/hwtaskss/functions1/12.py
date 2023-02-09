def histogram(list):
    for i in list:
        print( '*' * i)
a = [int(s) for s in input().split()]
histogram(a)