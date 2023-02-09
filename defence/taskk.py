n = int(input())
st = ""
pb = " "
i = 1
while i <=n :
    st += str(i)
    i += 1
    print((n - i + 1)  * pb + st)