my_tuple = (0, 1, 2, "hi", 4, 5)

# Your code here...


print(my_tuple)
midtuple = (3,)
my_tuple = my_tuple[0:3] + midtuple + my_tuple[4:6]
print(my_tuple)