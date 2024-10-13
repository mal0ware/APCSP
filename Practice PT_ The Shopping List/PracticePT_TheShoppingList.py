#Shopping List by Marius Castillo
print("Today, we are making the ultimate sandwich.")

ing_list = [] #user input recipe
pantry = ["Bread", "Nutella", "Jelly", "Butter", "Sugar", "Cinnamon", "Vodka", ] #pre-made pantry
req = [] #difference between them

def format_word(word): #to format the input correctly
    word = list(word)#break it down into letters
    for i_word, value_word in enumerate(word):
        if i_word == 0:
            word[i_word] = value_word.upper()
        else:
            word[i_word] = value_word.lower()
    word = ''.join(word) #regroup letters as a string
    return word
def is_complete(ing_list): #to compare inputs to the pantry
    for i_list, value_list in enumerate(ing_list):
        if value_list not in pantry:
            req.append(ing_list[i_list])
    if not req:
        print("It looks like you have everything to make your recipe!")
    else:
        print("The following ingredients are missing: ")
        for value_req in req:
            print(value_req)

while True: #loop to put stuff in the ingredient list
    word = format_word(input("Please enter an ingredient ('done' when complete): "))
    if word != "Done":
        ing_list.append(word)
    else:
        break #to break when the user IS done
is_complete(ing_list)