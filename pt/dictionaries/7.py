a = {}
for i in range(int(input())):
    words = [s for s in input().split()]
    a[words[0]] = words[1:]
for i in range(int(input())):
    x = input()
    for elem in a:
        if x in a[elem]:
            print(elem)
