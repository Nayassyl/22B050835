a = [int(s) for s in input().split()]
s = set()
for num in a:
    if num in s:
        print("YES")
    else:
        print("NO")
        s.add(num)
