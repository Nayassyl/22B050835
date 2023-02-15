n = int(input())
listt = []
al = set()
one = set()
for i in range(n):
    x = int(input())
    for j in range(x):
        listt.append(input())
    al |= set(listt)
    one = set(listt) & al
    listt.clear()
print(len(one))
for elem in sorted(one):
    print(elem)
print(len(al))
for elem in sorted(al):
    print(elem)

