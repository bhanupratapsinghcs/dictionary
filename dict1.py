# BASIC DICTIONARY

# importing library
import json
# loading json data as dictionary in Python
data = json.load(open("words.json"))


# function
def getMeaning(word):
    return data[word]


# taking input from user
userWord = input("Enter a word: ")
print(getMeaning(userWord))
