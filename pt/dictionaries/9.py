a = {}
for i in range(int(input())):
    word = input()
    base = word.lower()
    if base not in a:
        a[base] = set()
    a[base].add(word)
cnt = 0
hw = input().split()
for elem in hw:
    base = elem.lower()
    if (base in a and elem not in a[base]) or len([s for s in elem if s.isupper()]) != 1:
            cnt += 1
print(cnt)