"""
 Write a program that guesses every possible 4 digit passcode
 combinations until the correct passcode is guessed.

 The passcode is randomly generated and stored in the variable
 secretPasscode.

 Print out how many guesses it took to guess the correct passcode.
"""
import random

# Checks whether the given guess passcode is the correct passcode
def is_correct(guess_code, correct_code):
    return guess_code == correct_code

# Generates a random 4 digit passcode and returns it as a String
def generate_random_passcode():
    random_passcode = ""
    
    for i in range(4):
        random_digit = random.randint(0, 9)
        random_passcode += str(random_digit)
    return random_passcode

secret_passcode = generate_random_passcode()
# Write your code here
def guessEveryPossiblePasscode(secret_passcode):
    numGuesses = 0
    for firstDigit in range(10):
        for secondDigit in range(10):
            for thirdDigit in range(10):
                for fourthDigit in range(10):
                    currentGuess = str(firstDigit) + str(secondDigit) + str(thirdDigit) + str(fourthDigit)
                    numGuesses+=1
                    if is_correct(currentGuess, secret_passcode):
                        print("Passcode: " + str(currentGuess))
                        print("It took " + str(numGuesses) + " guesses to find the correct passcode.")
guessEveryPossiblePasscode(secret_passcode)