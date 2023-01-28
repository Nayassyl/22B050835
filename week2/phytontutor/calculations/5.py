n = int(input())

m = n * 45 
if n % 2 == 0:
    m += ( n / 2 ) * 5 + ((( n / 2 ) - 1 ) * 15)
else:
     m += ((n - 1) / 2) * 20
h = int( m / 60)
m %= 60

print ( 9 + h , int(m))