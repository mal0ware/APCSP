#local variables are variables that only pertain to the inner working of a function.
#local variables do not affect those outside of a function unless returned
#the scope is local for things inside the function
x = 0 #global x
def funk(x):#everything indented is local
    x = 5
    return x #The scope is local for this x
x = funk(x) #assigns the local x to global x
print(x)