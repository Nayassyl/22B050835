n = int(input())
i = 1
st = ""
while i <= n:
    st += str(i)
    i += 1

while n > 0:
    print(st)
    st = st.replace(str(n), " ")
    n -= 1