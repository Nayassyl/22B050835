a = float(input())

h = int(a // 30)
m = int(((a % 30) * 120) // 60 )
s = int(((a % 30) * 120) % 60 )
print (h , m , s)