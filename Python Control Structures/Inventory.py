STARTING_ITEMS_IN_INVENTORY = 20

num_items = STARTING_ITEMS_IN_INVENTORY
buy = 0
# Enter your code here
while num_items > 0:
    print("We have", num_items, "items in inventory.", sep = " ")
    buy = int(input("How many would you like to buy? "))
    if buy <= num_items:
        num_items -= buy
        if num_items > 0:
            print("Now we have", num_items, "left.", sep=" ")
    else:
        print("There is not enough in inventory for that purchase.")
print("All out!")