n = int(input())
s = set(i for i in range(1, n + 1))
while True:
    x = input()
    if x == "HELP":
        break
    answer = input()
    x = {i for i in x.split()}
    if answer == "YES":
        s &= x
    elif answer == "NO":
        s -= x
for elem in s:
    print(elem)

