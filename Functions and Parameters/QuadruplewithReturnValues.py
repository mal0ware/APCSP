# Defines Quadruple Function
def quadruple(x):
    answer = x * 4
    return answer

#Fodder for checking
print("5 quadrupled is:")
y = quadruple(5)
print(y)

print("10 quadrupled is:")
y = quadruple(10)
print(y)

#User Input
print("Try inputing a number: ")
y = quadruple(int(input()))
print("That number quadrupled is:")
print(y)