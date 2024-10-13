text = input("Enter some text: ")
indices = [ ]
count = 0
wordList = text.split()
for owl, word in enumerate(wordList):
    if "owl" in word:
        indices.append(owl)
        count += 1
print("There were", count, "word that contained 'owl'. ")
print("They occured at indices: ", indices)