import random
z = 0
while True:
    x = random.randint(1,6)
    y = random.randint(1,6)
    print("Rolled: " + str(x) + " " + str(y))
    z += 1
    if x == 1 and y == 1:
        break
print("It took " + str(z) + " tries to get Snake eyes!")