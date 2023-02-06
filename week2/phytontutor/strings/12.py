s = input()
a = ""
for x in range(len(s)):
    if x % 3 != 0:
        a += s[x]
print(a)