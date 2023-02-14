from math import hypot
def distance(x1, y1, x2, y2):
    return hypot(abs(x2 - x1), abs(y2 - y1))

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
print(distance(x1, y1, x2, y2))