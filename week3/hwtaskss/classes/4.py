from math import hypot
class Point:
    def __init__(self, x , y):
        self.x = x
        self.y = y

    def show(self, x , y): 
        print( str(self.x) ,  str(self.y))
    def distance( self, x1 , y1 ):
        n = abs(self.x - x1)
        m = abs(self.y - y1)
        print( hypot( n, m) )
    def move(self, moveforx , movefory):
        movex = self.x + moveforx
        movey = self.y + movefory
        print( str(movex) ,  str(movey))

x , y = [int(s) for s in input("Coordinates of first point: ").split() ]
mx, my = [int(s) for s in input("Values to move point for x and y: ").split() ]
x1, y1= [int(s) for s in input("Coordinates of second point: ").split() ]
s = Point( x , y)
print("Our cootdinates:")
s.show(x, y)
print("Moved coordinates: ")
s.move(mx, my)
print("Distance: ")
s.distance(x1, y1)









