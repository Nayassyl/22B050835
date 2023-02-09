class Shape:
    def __init__(self):
        pass
    def area():
        return 0
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.l = length
    def area(self):
        return self.l * self.l

x = int(input())
s = Square(x)
print(s.area())
