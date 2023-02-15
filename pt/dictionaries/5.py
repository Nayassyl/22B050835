n = int(input())
a = {}
for i in range(n):
    files = [s for s in input().split()]
    for j in range(len(files)):
        if files[j] == "R":
            files[j] = 'read'
        elif files[j] == "W":
            files[j] = 'write'
        elif files[j] == "X":
            files[j] = 'execute'
    a[files[0]] = files[1:]
for i in range(int(input())):
    x, y = input().split()
    if x in a[y]:
        print("OK")
    else:
        print("Access denied")

    