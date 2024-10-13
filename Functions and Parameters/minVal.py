a = 0 #first value
b = 0 #second value

def minVal(a, b):
    if a != b:#just in case they are the same value
        if a > b:
            return b
        else:#a<b
            return a
    else:
        return a

a = int(input("First Value: "))
b = int(input("Second Value: "))
x = minVal(a, b)#calls function with given parameters
x = minVal(a, b)#fodder for checking

print("The min is " + str(x))