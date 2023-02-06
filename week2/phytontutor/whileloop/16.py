x = int(input())
cnt = 0
maxcnt = 0
while x != 0:
    a = x
    x = int(input())
    if x == a:
        cnt += 1
    else:
        if cnt > maxcnt:
            maxcnt = cnt
        cnt = 0
print(maxcnt + 1)