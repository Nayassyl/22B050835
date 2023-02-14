class Vehicle:
    def __init__(self, engine):
        self.e = engine
    def printInfo(self):
        print(self.e)
class Car(Vehicle):
    def __init__(self, engine, mark, color):
        super().__init__(engine)
        self.m = mark
        self.col = color
    def printInfo(self):
        print(self.e, self.m, self.col)
class Toyota(Car):
    def __init__(self, engine, mark, color, country):
        super().__init__(engine, mark, color)
        self.cou = country
    def printInfo(self):
        print(self.e, self.m, self.col, self.cou)
    def getter(self):
        self.price = int(input())
    def setter(self):
        print(self.price)

v = Vehicle("enginee")
v.printInfo()
#v.getter()
#v.setter()

