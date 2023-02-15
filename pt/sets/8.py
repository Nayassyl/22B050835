n = int(input())
s = set(i for i in range(1, n + 1))
while True:
    x = input()
    if x == "HELP":
        break
    x = {i for i in x.split()}
    if len(s & x) <= len(s)/2:
        print("NO")
        s -= x
    else:
        print("YES")
        s &= x
for elem in s:
    print(elem)
