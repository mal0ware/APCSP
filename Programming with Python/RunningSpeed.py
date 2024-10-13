# Enter your code here
milesRan = int( input("How many miles did you run? "))
minutesTaken = int( input("How many minutes did it take you? "))
speedInMph = milesRan/(minutesTaken/60)
print("Speed in mph", speedInMph, sep=" ", end="\n")