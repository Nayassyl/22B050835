
p = float(input())
x = float(input())
y = float(input())

m = x * 100 + y
m = int( m * ( p + 100)/100)

print (m // 100, m % 100)