class Person:
    def __init__(self, name, nationality):
        self.name = name 
        self.nationality = nationality
    def printInfo(self):
        print(self.name , self.nationality)
    def setSurname(self):
        self.surname = input()
    def getSurname(self):
        print(self.surname)

class Student(Person):
    def __init__(self, name, nationality, id):
        super().__init__(name, nationality)
        self.id = id
    def printInfo(self):
        print(self.name, self.nationality, self.id)

class Teacher(Person):
    def __init__(self, name, nationality, teacher_id):
        super().__init__(name, nationality)
        self.teacher_id = teacher_id
    def printInfo(self):
        print(self.name, self.nationality, self.teacher_id) 

obj1 = Student("Diar", "Kazakh", "00000000")
obj1.printInfo()

obj2 = Teacher("Arnur", "Kazakh", "00000000")
obj2.printInfo()

objj = Person("Diar", "Kazakh")
objj.setSurname()
objj.getSurname()
objj.printInfo()