import random
name = input("Hello! What is your name?\n")
print("Well, " + name + ", I am thinking of a number between 1 and 20.")
numm = int(random.randint(1, 20))
x = int(input("Take a quess.\n"))
cnt = 1

while x != numm:
    if x < numm:
        print("Your guess is too low.")
    elif x > numm:
        print ("Your guess is too high.")
    x = int(input("Take a guess.\n"))
    cnt += 1

print("Good job," + name + "! You guessed my number in " + str(cnt) + " guesses!")