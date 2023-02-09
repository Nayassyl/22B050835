class stt():
    def __init__(self):
        self.str = ""

    def get_String(self):
        self.str = input()

    def print_String(self):
        print(self.str.upper())

str1 = stt()
str1.get_String()
str1.print_String()