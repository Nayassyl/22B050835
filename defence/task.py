n = int(input())
i = n
st = ""
while i > 0:
    st += str(i)
    i -= 1
l = n
while l > 0:
    print(st)
    l -= 1
    k = n - l
    st = st.replace(str(k), " ")

i = n
pb = " "
st = ""
while i > 0:
    st += str(i)
    i -= 1
l = n
while l > 0:
    print( pb * (n - l) + st)
    l -= 1
    k = n - l
    st = st.replace(str(k), " ")

