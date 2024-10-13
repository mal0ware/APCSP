lastnames = []
for i in range(5):
    name = input("Name: ")
    name_parts = name.split()
    last_name = name_parts[-1]
    lastnames.append(last_name)
lastnames.sort()
print(lastnames)