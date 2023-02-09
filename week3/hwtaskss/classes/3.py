class Shape:
    def __init__(self):
        pass
    def area():
        return 0
class Rectangle(Shape):
    def __init__(self, length, width ):
        super().__init__()
        self.l = length
        self.w = width
    def area(self):
        return self.l * self.w

x , y = [int(s) for s in input().split() ]
s = Rectangle(x , y)
print(s.area())
