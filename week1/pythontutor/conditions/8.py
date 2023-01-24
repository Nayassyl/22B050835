x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if( ((x2-x1) == 1 or (x2-x1) == -1 or (y2-y1) == 1 or (y2-y1) == -1) and ((x1+y1) - (x2+y2) <= 2 and (x1+y1) - (x2+y2) >= -2 )):
    print("YES")
else:
    print("NO")