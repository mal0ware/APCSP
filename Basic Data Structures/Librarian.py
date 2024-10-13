print("enter 5 names!")
names = [ ]
for i in range(5):
    names.append(input("Enter Name: "))
    print(names)
print("Now here are the names, sorted!")
names.sort()
print(names)