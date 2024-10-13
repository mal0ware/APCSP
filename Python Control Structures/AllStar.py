# Enter your code here

points = int(input("Points per game? "))
rebounds = int(input("Rebounds per game? "))
assists = int(input("Assists per game? "))
is_allstar = points >= 25 or (points >= 10 and rebounds >= 10 and assists >= 10)
print("Is all star? " + str(is_allstar))