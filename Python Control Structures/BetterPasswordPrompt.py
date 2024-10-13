SECRET = "abc123"

while True:
    x = input("Enter password: ")
    if x == SECRET:
        break
    else:
        print("Sorry, that did not match. Please try again.")
        continue
print("You got it!")