"""
1. Ask your friend for an initial word
2. Repeatedly ask them for an index and a letter (Functions)
3. You should replace the letter at the index they provided with the letter they enter
4. You should then print the new word
5. Stop asking for input when the user enters -1 for the index

Heres what should be happening behind the scenes:

You should have a function, get_index , that repeatedly asks the user for an index until they enter a valid integer 
that is within the acceptable range of indices for the initial string. 
(If they enter a number out of range, you should reply invalid index.)

You should have another function, get_letter , that repeatedly asks the user for a letter
until they enter exactly one lowercase letter. (If they enter more than one character, 
you should reply Must be exactly one character!. If they enter a capital letter,
you should reply Character must be a lowercase letter!.)

You should store a list version of the current word in a variable. 
This is what you should update each time the user swaps out a new letter.
Each time you have to print the current word, 
print the string version of the list you are keeping in your variable.
"""

def get_index(max_index):
    while True:
        try:
            index = int(input("Enter an index (-1 to quit): "))

            if index == -1:
                return index
            if 0 <= index < max_index:
                return index
            else:
                print("Invalid index")
                
        except ValueError:
            print("Invalid input. Please enter a valid integer index.")

def get_letter():
    while True:
        letter = input("Enter a letter: ")
        if len(letter) == 1 and letter.islower():
            return letter
        elif len(letter) != 1:
            print("Must be exactly one character!")
        elif letter.islower() == False:
            print("Character must be a lowercase letter!")
        else:
            print("get_letter function error")


#MAIN
word = input("Enter a word: ")
word_list = list(word)

while True:
    index = get_index(len(word))
    if index == -1:
        break
    letter = get_letter()
    word_list[index] = letter
    word = "".join(word_list)
    print(word)