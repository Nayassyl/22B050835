n = int(input())
m = int(input())
k = int(input())

if( (((n * m) - k) % n == 0 or ((n * m) - k) % m == 0) and k <= (n * m)):
    print("YES")
else:
    print("NO")