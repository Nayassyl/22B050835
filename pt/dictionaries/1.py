a={}
for word in input().split():
    if word in a:
        a[word] += 1
        print(a[word], end = " ")
    else:
        a[word]=0
        print(a[word], end = " ")
