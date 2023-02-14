import random
def kk(n):
    secret = int(random.randint(1, n))
    l = set()
    s = set()
    while input() != "HELP":
        s.update(int(input().split))
        if secret in s:
            print("YES")
            l.update(s)
        else:
            print("NO")
            l.difference_update(s)
    for i in l: print (i)

n = int(input())
kk(n)

