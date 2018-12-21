# FINDING THE CLOSEST WORDS

# import library
import json

from difflib import get_close_matches    # Text processing services
# loading json formated data into dictionary format in Python
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
        return "Did you mean %s instead?" % get_close_matches(word, data.keys())[0]
                                        # [0] means the first value of all similar values


userWord = input("Enter a word: ")
print(getMeaning(userWord))
