# Enter your code here

#constant
COST_OF_FRISBEES = 15
wantedFrisbees = int(input("How many many frisbees do you want? "))
totalCost = COST_OF_FRISBEES * wantedFrisbees
print("That'll be",totalCost, "dollars for",wantedFrisbees, "frisbees", sep=" ", end="\n")