# Defining the Function
def square(x):
    y = x * x
    return y
    
# Fodder for checking
print("5 squared is")
x = square(5)
print(x)
print("6 squared is")
x = square(6)
print (x)

# Some User Input
print("Input your own number: ")
print("Now That squared, is:", square(int(input())))