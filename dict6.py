# CLEAN OUTPUT INSTEAD OF LISTS

# import library
import json

from difflib import get_close_matches     # Text processing services
# loading json formatted data into dictionary format in Python
data = json.load(open("words.json"))


# function
def getMeaning(word):
    word = word.lower()    # converting user input into lower case

    if word in data:         # checking for normal words
        return data[word]
    elif word.title() in data:      # checking for words starting with capital letters
        return data[word.title()]
    elif word.upper() in data:      # checking for words woth all CAPS
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:       # printing the values which are nearly similar
        action = input("Did you mean %s instead? [y or n]:" % get_close_matches(word, data.keys())[0])
                                        # [0] means the first value of all similar values
        if action == "y":
            return data[get_close_matches(word,data.keys())[0]]
        elif action == "n":
            return "The word doesn't exist"
        else:
            return "Wrong entry"


userWord = input("Enter a word: ")
output = getMeaning(userWord)
# if word has more than one meaning, print them in new lines
if type(output) == list:
    for item in output:
        print("-" + item)
else:
    print("-" + output)