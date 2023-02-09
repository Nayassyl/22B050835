class Account:
    def __init__(self, owner, balance = 0):
        self.o = owner
        self.b = balance
    def deposit(self, deposit):
        self.b += deposit
        print( "Your balance: " + str(self.b) + " tg")
    def withdraw(self, withdraw):
        if withdraw > self.b:
            print("Sorry, you don't have such amount of money.")
        else:
            self.b -= withdraw
            print(str(withdraw) + " dollars was withdrawn")
            print("Your balance: " + str(self.b) + " tg")

name = Account("Nursaya")
name.deposit(36660) 
x = int(input()) 
name.withdraw(x)

