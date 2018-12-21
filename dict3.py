# CASE SENSITIVITY

# import library
import json
# loading data in json format as dictionary formart in Python
data = json.load(open("words.json"))


# function for checking all CAPS and all lowers
def getMeaning(word):
    word = word.lower()     # converting all letters to lower case
    if word in data:        # checking if normal word is in data
        return data[word]
    elif word.title() in data:    # checking if words starting with capital letter are in data)
        return data[word.title()]
    elif word.upper() in data:    # checking if words with all CAPS are in data
        return data[word.upper()]
    else:
        return "No such word exists"


userWord = input("Enter a word: ")
print(getMeaning(userWord))
