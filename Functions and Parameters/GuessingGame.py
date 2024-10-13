import random

x = random.randint(1,100) #random number generator
y = -1 #userinput var

while y != x: #reprompt until correct
    try:
        y = int(input("Guess: "))
        if y > x:
            print("Too high")
        elif y < x:
            print("Too low")
    except ValueError: #catches errors
        print("Please input a valid integer.")
print("Correct!")