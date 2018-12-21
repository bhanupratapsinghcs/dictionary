# INTERACTIVE DICTIONARY

# import required libraries
import json    # data required for dictionary i.e meanings of al the words from server
from difflib import get_close_matches    # Text-processing services

# loading the data stored in json format as dictionary format in Python
data = json.load(open("words.json"))


# function for getting the meaning
def getMeaning(word):
    word = word.lower() # converting user input into lower cases

    if word in data:    # checking all normal words
        return data[word]
    elif word.title() in data:    # checking words starting with Caps
        return data[word.title()]
    elif word.upper() in data:    # checking words with all the capitals
        return data[word.upper()]
    # finding the closest matches of the words if they are not in the data
    elif len(get_close_matches(word, data.keys())) > 0:
        action = input("Do you mean %s instead? [y or n]: " % get_close_matches(word, data.keys())[0])
        # if the input user gave is y i.e yes get the meaning of suggested word
        if action == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif action == "n":
            return "There is no such word"
        else:
            return "Wrong input"


# output
userWord = input("Enter a word: ")
output = getMeaning(userWord)
# if word has more than one meaning print them in new lines
if type(output) == list:
    for item in output:
        print("-" + item)
else:
    print("-" + output)